import os
from sqlalchemy import text

from eme.data_access import get_repo

from modules import modules

from core.dal.base.sqlite import EntityBase
from core.dal.ctx import db_session, db_engine, db_type


def migrate_db(autoclear=False, autofixtures=False):
    # check if DB is populated
    if not check_db():
        print("The database is not empty. Drop tables? Y/n:", end="")

        if autoclear or input().lower() == 'y':
            print("Dropping tables")
            EntityBase.metadata.drop_all(db_engine)
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
            EntityBase.metadata.drop_all(db_engine)

    base = 'modules/eme_utils/migrations/' + db_type + '/'
    try:
        files = os.listdir(base)
    except:
        files = []

    conn = db_session.connection()

    # SQLAlchemy migration
    print("Applying SQLAlchemy migrations...")
    from core.dal import migration

    for module in modules:
        if hasattr(module, 'init_dal'):
            module.init_dal()
        if hasattr(module, 'init_migration'):
            module.init_migration()

    EntityBase.metadata.create_all(db_engine)

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
    base = 'modules/eme_utils/migrations/' + db_type + '/'

    with open(os.path.join(base, f), 'r') as sql_file:
        sql = text(sql_file.read())

    result = conn.execute(sql)

    db_session.commit()
    conn.close()


def check_db():
    for module in modules:
        if hasattr(module, 'is_empty'):
            if not module.is_empty():
                return False
    else:
        return True


def clear_db():
    for module in modules:
        if hasattr(module, 'clear_db'):
            module.clear_db()
