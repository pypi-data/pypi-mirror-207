import importlib
import itertools
import logging
import pkgutil
import re
from dataclasses import dataclass
from operator import attrgetter
from pathlib import Path
from typing import Optional

from faunadb import query
from faunadb.client import FaunaClient

logger = logging.getLogger(__name__)


@dataclass
class Migration:
    """A simple dataclass for defining a migration with a name and operations to
    perform.

    name: The name of the migration.

    namespace: The namespace this migration lives under. This is used to prevent naming
               collisions of migrations applied to the same database from different
               projects.

    migration: The actual FQL to run when performing the migration.

    reverse_migration: The FQL that undoes the FQL applied in the migration step.

    child_database: An optional child database to apply this migration to. The child
                    database name follows the same nesting rules as FaunaDB scoped keys.
                    The child database name is considered relative to the database of
                    the key used to invoke the migration process.
    """

    name: str
    namespace: str
    migration: query
    reverse_migration: query
    child_database: Optional[str] = None

    @property
    def full_name(self):
        """Return the namespace and name concatenated as f"{namespace}.{name}"."""
        return f"{self.namespace}.{self.name}"

    def __str__(self):
        """Return the namespace and name concatenated as "<namespace>.<name>"."""
        return self.full_name


# Make public the names of the created migrations collection and index in case anyone
# outside this module needs it.
migrations_collection_name = "fluctuate_migrations"
migrations_index_name = "fluctuate_migrations_unique_name_and_namespace"

# This contains the query used to check if the migrations collection already exists, and
# creates it if it doesn't.
_create_migrations_collection = query.if_(
    query.exists(query.collection(migrations_collection_name)),
    query.get(query.collection(migrations_collection_name)),
    query.create_collection({"name": migrations_collection_name, "history_days": 0}),
)

# This contains the query used to check if the unique constraint on migrations already
# exists, and creates it if it doesn't.
_create_migrations_unique_index = query.if_(
    query.exists(query.index(migrations_index_name)),
    query.get(query.index(migrations_index_name)),
    query.create_index(
        {
            "name": migrations_index_name,
            "source": query.select("ref", query.var("collection")),
            "terms": [
                {"field": ["data", "name"]},
                {"field": ["data", "namespace"]},
            ],
            "unique": True,
        }
    ),
)

# Combines the two previously defined queries using let. This is required because of the
# fact that schema documents cannot be created and then referenced in the same query.
# Details here: https://forums.fauna.com/t/do-and-creation-of-schema-documents/3418
_create_required_migrations_schema_objects = query.let(
    {"collection": _create_migrations_collection}, _create_migrations_unique_index
)


def _create_fauna_client(key, child_db=None):
    """Create the FaunaDB client using the provided key and return it.

    This configures the FaunaDB client to use the US region group:
    https://docs.fauna.com/fauna/current/learn/understanding/region_groups#how-to-use-region-groups

    If a `child_db` is provided, the client created will be scoped to that child
    database.

    If a `child_db` is provided and the `key` provided is itself a scoped key, the
    resulting key used to create the client will retain the role of the scoped key.
    The child database will also be appended to any child databases the provided key is
    already scoped to.
    """
    # If this is for a child DB, we need to create a scoped key to bind the client to
    # the child DB.
    if child_db is not None:
        key = _build_scoped_key(key=key, child_db=child_db)
        logger.debug("Creating FaunaDB client for child database %s.", child_db)
    else:
        logger.debug("Creating FaunaDB client for top level database.")

    fauna_client = FaunaClient(secret=key, domain="db.us.fauna.com")
    logger.debug("FaunaDB client initialized.")

    return fauna_client


# This FQL fragment matches the fluctuate_migrations_unique_name_and_namespace using the variables
# "migration_name" and "migration_namespace" to retrieve the migration's name and
# namespace, respectively.
_match_on_name_and_namespace = query.match(
    query.index(migrations_index_name),
    [query.var("migration_name"), query.var("migration_namespace")],
)


def _filter_migrations(fauna_client, migrations, condition):
    """Filter to migrations matching the provided condition expression.

    The condition expression will be passed the variables of "migration_full_name",
    "migration_name", and "migration_namespace".
    """
    filtered_migrations = fauna_client.query(
        query.filter_(
            query.lambda_(
                ["migration_full_name", "migration_name", "migration_namespace"],
                condition,
            ),
            tuple(
                (migration.full_name, migration.name, migration.namespace)
                for migration in migrations
            ),
        )
    )
    # Turn it into a tuple of just the full names.
    filtered_migrations = tuple(migration[0] for migration in filtered_migrations)

    # We should return the migrations list based on which migrations came back.
    return tuple(
        migration
        for migration in migrations
        if migration.full_name in filtered_migrations
    )


def _filter_unapplied_migrations(fauna_client, migrations):
    """Filter the migrations tuple to the migrations that are not yet applied."""
    logger.debug(
        "Filtering the following migrations down to ones that are not applied: %s",
        migrations,
    )

    # We should return the migrations list based on which migrations came back as
    # unapplied.
    result = _filter_migrations(
        fauna_client=fauna_client,
        migrations=migrations,
        condition=query.not_(query.exists(_match_on_name_and_namespace)),
    )
    logger.debug("Found the following unapplied migrations: %s", result)

    return result


def _filter_applied_migrations(fauna_client, migrations):
    """Filter the migrations tuple to the migrations that are already applied."""
    logger.debug(
        "Filtering the following migrations down to ones that are applied: %s",
        migrations,
    )

    # We should return the migrations list based on which migrations came back as
    # applied.
    result = _filter_migrations(
        fauna_client=fauna_client,
        migrations=migrations,
        condition=query.exists(_match_on_name_and_namespace),
    )
    logger.debug("Found the following applied migrations: %s", result)

    return result


def _write_migration_document(migration):
    """Write the migration name to the migrations table."""
    migration_data = {
        "name": migration.name,
        "namespace": migration.namespace,
        "child_database": migration.child_database,
    }
    logger.debug("Create migration record: %s", migration_data)

    return query.create(
        query.collection(migrations_collection_name), {"data": migration_data}
    )


def _delete_migration_document(migration):
    """Delete the migration name in the migrations table."""
    migration_tuple = (migration.name, migration.namespace)
    logger.debug("Delete migration tuple: %s", migration_tuple)

    return query.delete(
        query.select(
            "ref",
            query.get(query.match(query.index(migrations_index_name), migration_tuple)),
        )
    )


def _log_package_import_error(module_name):
    """This logs that a module failed to be imported during discovery at the debug
    level to aid in debugging migration discovery issues.
    """
    logger.debug(
        "Failed to import module named %s during migration discovery. If the migrations"
        " were in this module, they will not be discovered.",
        module_name,
    )


def _find_migrations_module():
    """Find the migrations module by walking packages in the current working directory.

    If a suitable candidate module is found, it is returned. Otherwise `None` is
    returned.
    """
    # Find the expected module name in the available modules.
    migrations_module_name = None
    cwd = str(Path.cwd())
    logger.debug("Searching for migration modules in %s.", cwd)
    for _, name, _ in pkgutil.walk_packages(
        path=[cwd], onerror=_log_package_import_error
    ):
        logger.debug("Walking module named %s.", name)
        if migrations_collection_name in name:
            migrations_module_name = name
            logger.debug(
                "Found migration module candidate named %s.", migrations_module_name
            )
            break

    if migrations_module_name is None:
        logger.debug("No migration module candidates found.")
        return None

    # Import it and grab the migrations if present.
    logger.debug("Importing module named %s.", migrations_module_name)
    return importlib.import_module(name=migrations_module_name)


def _is_valid_migrations_module(migrations_module):
    """Validate that the migrations module contains fluctuate migrations."""
    logger.debug(
        "Validating if module %s contains valid fluctuate migrations.",
        migrations_module.__name__,
    )

    if not hasattr(migrations_module, "migrations"):
        logger.debug(
            "No migrations attribute found in module named %s.",
            migrations_module.__name__,
        )
        return False

    if not isinstance(migrations_module.migrations, (tuple, list)):
        logger.debug("The migrations attribute is not a tuple or list.")
        return False

    if not migrations_module.migrations:
        logger.debug("The migrations attribute is empty.")
        return False

    if not all(
        isinstance(migration, Migration) for migration in migrations_module.migrations
    ):
        logger.debug(
            "The migrations attribute does not solely contain Migration objects."
        )
        return False

    logger.debug(
        "Validated that module %s contains valid fluctuate migrations.",
        migrations_module.__name__,
    )
    return True


def _discover_migrations():
    """This method discovers the migrations under the current working directory and
    returns them.

    The convention is to have a module named migrations_collection_name that contains a
    member named "migrations". This should either be a tuple or list of `Migration`
    dataclass objects.
    """
    migrations_module = _find_migrations_module()
    if migrations_module is None:
        return tuple()

    if not _is_valid_migrations_module(migrations_module=migrations_module):
        return tuple()

    return migrations_module.migrations


def _build_scoped_key(key, child_db):
    """Build a key scoped to the provided child_db name.

    If the key provided is a top level key, the result will be a scoped key of the form
    f"{key}:{child_db}:admin".

    If the key provided is itself a scoped key *without* a child database defined, the
    result will be a scoped key of the form
    f"{key portion of the scoped key}:{child_db}:{role of the scoped key}".

    If the key provided is itself a scoped key *with* a child database defined, the
    result will be a scoped key of the form
    f"{key portion of the scoped key}:{child database(s) of the scoped key}/{child_db}:{role of the scoped key}".
    """
    scoped_key_regex = r"""
        # Perform a non-greedy match from the beginning of the string to the next `:` to
        # extract the key.
        (?P<key>^.+?)
        # Optional child database group. Performs same non-greedy match as the key
        # group to match to the next `:` to extract the child database this key is
        # scoped to.
        (:(?P<child_database>.+?))?
        # Role group that matches from the last `:` to the end of the string.
        :(?P<role>.+)$
    """
    logger.debug("Checking if the provided key is a scoped key.")
    result = re.match(pattern=scoped_key_regex, string=key, flags=re.VERBOSE)

    # Default to the admin role.
    role = "admin"

    # If the key turns out to be a scoped key, we need to do some extra work.
    if result is not None:
        logger.debug("Provided key is a scoped key.")
        # Pull the actual key portion out of the scoped key.
        key = result.group("key")
        parents = result.group("child_database")
        # Override the default role with the role provided by the scoped key.
        role = result.group("role")

        # If the key is already scoped to a child database, assume that the `child_db`
        # passed in is a child of the child DB the passed in `key` is scoped to.
        if parents is not None:
            logger.debug(
                "Provided key is already scoped to child database(s) %s.", parents
            )
            child_db = f"{parents}/{child_db}"

    logger.debug("Built scoped key for child database %s with role %s.", child_db, role)
    return f"{key}:{child_db}:{role}"


def _ensure_child_db(key, child_db):
    """Ensure that the child DB exists before proceeding further.

    If there are multiple child DBs, I.E. the `child_db` parameter is of the form
    "child1/child2/child3", then each DB is checked for existence.
    """
    logger.debug("Ensuring that all child dbs in %s exist.", child_db)
    # Split the children into individual scoped key paths so we can log into each child
    # DB individually. For example: "child1/child2/child3" becomes
    # `("child1", "child1/child2", "child1/child2/child3")`
    child_db_names = child_db.split("/")
    child_db_full_paths = tuple(
        itertools.accumulate(
            iterable=child_db_names,
            func=lambda child1, child2: "/".join((child1, child2)),
        )
    )
    # Get the full paths of the what would be the parents of each child DB by adding
    # None to the beginning of the child DB full paths. None signifies the parent is the
    # DB which the provided key gives us access to, thus not requiring a scoped key.
    child_db_full_paths_parent = (None, *child_db_full_paths)

    # We rely on zip stopping once the shortest iterable is exhausted. This means we
    # never fully iterate over `child_db_full_paths_parent`, as we always want to log
    # into the parent of the child DB we are checking for the existence of.
    for child_db_name, child_db_full_path, child_db_parent_full_path in zip(
        child_db_names, child_db_full_paths, child_db_full_paths_parent
    ):
        fauna_client = _create_fauna_client(key=key, child_db=child_db_parent_full_path)
        # Ensure the child DB exists.
        if not fauna_client.query(query.exists(query.database(child_db_name))):
            logger.debug("Child DB %s doesn't exist.", child_db_full_path)
            return False

        logger.debug("Child DB %s exists.", child_db_full_path)

    logger.debug("All child dbs in %s exist.", child_db)
    return True


def _target_in_migrations(target, migrations):
    """Returns whether the target migration is within the provided migrations."""
    if target in (migration.full_name for migration in migrations):
        return True

    return False


def _filter_to_migrations_up_to_target(target, migrations):
    """Filter the migrations to unapply down to the ones up to and including the target."""
    logger.debug(
        "Found target migration %s. Migrations to unapply before limiting to"
        " target: %s.",
        target,
        migrations,
    )
    # We need to remove all of the migrations that, in forward order, come
    # before the target migration so we don't unapply any migrations prior to
    # the target. To do this we (read from inside outward):
    # 1. Reverse the migrations to get them back into forward order. They were
    #    reversed previously to walk the migrations in reverse order in the caller.
    # 2. Drop all migrations until we reach the target migration so we are only
    #    left with the migrations to be unapplied.
    # 3. Re-reverse the migrations to get them back into reverse order as we
    #    want to unapply in reverse order from how they were applied.
    migrations = tuple(
        reversed(
            tuple(
                itertools.dropwhile(
                    lambda migration: target != migration.full_name,
                    reversed(migrations),
                )
            )
        )
    )
    logger.debug(
        "Migrations to unapply after limiting to target migration %s: %s.",
        target,
        migrations,
    )
    return migrations


def _apply_migration(fauna_client, migration):
    """Apply an individual migration and write the migration document to record its
    application.

    This is done in a single transaction so that if the migration should fail, no
    actions are taken.
    """
    logger.debug("Attempting to apply migration %s", migration.name)
    fauna_client.query(
        query.do(
            # Apply the migration.
            migration.migration,
            # Then record that the migration was applied.
            _write_migration_document(migration=migration),
        )
    )
    logger.debug("Successfully applied migration %s", migration.name)


def _apply_migrations(key, child_db, migrations):
    """Apply the provided migrations to the specified child_db using the provided key."""
    fauna_client = _create_fauna_client(key=key, child_db=child_db)

    logger.debug("Creating required schema documents for migration.")
    # Create the required migration schema documents. This cannot be done in the
    # same transaction as applying and recording the applied migrations due to the
    # issue noted here:
    # https://forums.fauna.com/t/do-and-creation-of-schema-documents/3418
    fauna_client.query(_create_required_migrations_schema_objects)

    # We need to determine which migrations still need to be applied.
    unapplied_migrations = _filter_unapplied_migrations(
        fauna_client=fauna_client, migrations=migrations
    )
    if not unapplied_migrations:
        if child_db is not None:
            logger.info("No migrations to apply for child database %s.", child_db)
        else:
            logger.info("No migrations to apply.")

        return

    # Apply the unapplied migrations and write the applied ones to the migrations
    # table so we do not try to apply them a second time.
    if child_db is not None:
        logger.info(
            "Attempting to apply %d unapplied migrations to child database %s.",
            len(unapplied_migrations),
            child_db,
        )
    else:
        logger.info(
            "Attempting to apply %d unapplied migrations.",
            len(unapplied_migrations),
        )

    # Apply each migration in its own transaction.
    for migration in unapplied_migrations:
        _apply_migration(fauna_client=fauna_client, migration=migration)

    if child_db is not None:
        logger.info(
            "Successfully applied %d unapplied migrations to child database %s.",
            len(unapplied_migrations),
            child_db,
        )
    else:
        logger.info(
            "Successfully applied %d unapplied migrations.",
            len(unapplied_migrations),
        )


def _unapply_migration(fauna_client, migration):
    """Unapply an individual migration and remove the associated migration document.

    This is done in a single transaction so that if the migration should fail, no
    actions are taken.
    """
    logger.debug("Attempting to unapply migration %s", migration.name)
    fauna_client.query(
        query.do(
            # Unapply the migration.
            migration.reverse_migration,
            # Then record that the migration was unapplied.
            _delete_migration_document(migration=migration),
        )
    )
    logger.debug("Successfully unapplied migration %s", migration.name)


def _unapply_migrations(key, child_db, migrations):
    """Unapply the provided migrations for the child_db.

    If the child DB does not exist, no action will be performed.

    If there are no applied migrations, no action will be performed.
    """
    # We must ensure the child DB exists before continuing as it may have already
    # been deleted by a prior unmigrate.
    if child_db is not None and not _ensure_child_db(key=key, child_db=child_db):
        logger.info(
            "Child database %s does not exist. Skipping the unapply of migrations"
            " for this child database.",
            child_db,
        )
        return

    fauna_client = _create_fauna_client(key=key, child_db=child_db)

    logger.debug("Creating required schema documents for migration.")
    # Create the required migration schema documents. This cannot be done in the
    # same transaction as unapplying and deleting the migration documents due to the
    # issue noted here:
    # https://forums.fauna.com/t/do-and-creation-of-schema-documents/3418
    fauna_client.query(_create_required_migrations_schema_objects)

    applied_migrations = _filter_applied_migrations(
        fauna_client=fauna_client, migrations=migrations
    )
    if not applied_migrations:
        if child_db is not None:
            logger.info("No migrations to unapply for child database %s.", child_db)
        else:
            logger.info("No migrations to unapply.")

        return

    # Unapply the applied migrations and delete the unapplied ones from the
    # migrations table so we do not try to unapply them a second time.
    if child_db is not None:
        logger.info(
            "Attempting to unapply %d applied migrations on child database %s.",
            len(applied_migrations),
            child_db,
        )
    else:
        logger.info(
            "Attempting to unapply %d applied migrations.",
            len(applied_migrations),
        )

    # Unapply each migration in its own transaction.
    for migration in applied_migrations:
        _unapply_migration(fauna_client=fauna_client, migration=migration)

    if child_db is not None:
        logger.info(
            "Successfully unapplied %d applied migrations on child database %s.",
            len(applied_migrations),
            child_db,
        )
    else:
        logger.info(
            "Successfully unapplied %d applied migrations.", len(applied_migrations)
        )


def migrate(key):
    """Applies all unapplied migrations to the database that the provided key has access
    to.
    """
    all_migrations = _discover_migrations()
    if not all_migrations:
        logger.info("No migrations found.")
        return

    # A migration can apply to a top level database or a potentially nested set of child
    # databases.
    for child_db, migrations in itertools.groupby(
        all_migrations, key=attrgetter("child_database")
    ):
        # The code used below expects to be able to loop through this multiple times, so
        # we need to change this from a generator to a tuple.
        migrations = tuple(migrations)
        _apply_migrations(key=key, child_db=child_db, migrations=migrations)


def unmigrate(key, target=None):
    """Unapplies all migrations up to `target`. If no `target` is provided, all
    migrations are unapplied.
    """
    all_migrations = _discover_migrations()
    if not all_migrations:
        logger.info("No migrations found.")
        return

    if target is not None and not _target_in_migrations(
        target=target, migrations=all_migrations
    ):
        raise ValueError(
            f"Target migration named {target} not found in discovered migrations."
        )

    # A migration can apply to a top level database or a potentially nested set of child
    # databases. We loop in reverse order when unmigrating.
    for child_db, migrations in itertools.groupby(
        reversed(all_migrations), key=attrgetter("child_database")
    ):
        # The code used below expects to be able to loop through this multiple times, so
        # we need to change this from a generator to a tuple.
        migrations = tuple(migrations)

        # If there is no target, we always want this false so we don't break out of the
        # loop early.
        target_found = target is not None and _target_in_migrations(
            target=target, migrations=migrations
        )
        # If the target is within this batch of migrations, we need to limit the
        # migrations we unapply to the ones up to and including the target migration.
        if target_found:
            migrations = _filter_to_migrations_up_to_target(
                target=target, migrations=migrations
            )

        _unapply_migrations(key=key, child_db=child_db, migrations=migrations)

        if target_found:
            logger.info("Reached target migration to unapply %s. Stopping.", target)
            break
