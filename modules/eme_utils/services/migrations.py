import os
from sqlalchemy import text

from core.dal import EntityBase, ctx, drop_order


def migrate_db(autoclear=False, autofixtures=False):
    from modules.modules import modules

    for module in modules:
        if hasattr(module, 'init_dal'):
            module.init_dal()

        if hasattr(module, 'init_migration'):
            module.init_migration()

    # check if DB is populated
    if not check_db():
        print("The database is not empty. Drop tables? Y/n:", end="")

        if autoclear or input().lower() == 'y':
            print("Dropping tables")

            # todo: later: drop only selected tables
            EntityBase.metadata.drop_all(ctx.db_engine, tables=drop_order())
        else:
            print("Truncate tables? Y/n:", end="")
            if autoclear or input().lower() == 'y':
                print("Clearing DB")
                clear_db()
            else:
                print("Migration omitted")
                return
    else:
        print("Drop tables? Y/n:", end="")

        if autoclear or input().lower() == 'y':
            print("Dropping tables")
            EntityBase.metadata.drop_all(ctx.db_engine, tables=drop_order())

    base = 'modules/eme_utils/migrations/' + ctx.db_type + '/'
    try:
        files = os.listdir(base)
    except:
        files = []

    conn = ctx.db_session.connection()

    # SQLAlchemy migration
    print("Applying SQLAlchemy migrations...")

    EntityBase.metadata.create_all(ctx.db_engine)

    # SQL-based migrations
    for f in files:
        print('Applying migration {}...'.format(f))
        run_sql_migration(conn, f)

    print("Add test entities? Y/n:", end="")
    if autofixtures or input().lower() == 'y':
        for module in modules:
            if hasattr(module, 'create_testentities'):
                module.create_testentities()

    print("Done")


def run_sql_migration(conn, f):
    base = 'modules/eme_utils/migrations/' + ctx.db_type + '/'

    with open(os.path.join(base, f), 'r') as sql_file:
        sql = text(sql_file.read())

    result = conn.execute(sql)

    ctx.db_session.commit()
    conn.close()


def check_db():
    from modules.modules import modules
    for module in modules:
        if hasattr(module, 'is_empty'):
            if not module.is_empty():
                return False
    else:
        return True


def clear_db():
    from modules.modules import modules
    for module in modules:
        if hasattr(module, 'clear_db'):
            module.clear_db()
