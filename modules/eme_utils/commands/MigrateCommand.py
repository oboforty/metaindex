from modules.eme_utils import migrate_db


class MigrateCommand:
    """
    Command to run migrations on database.
    """
    def __init__(self, cli):
        self.conf = cli.conf['migration']

    def run(self, autoclear:bool=False, autofixtures:bool=False):
        migrate_db(autoclear=autoclear, autofixtures=autofixtures)
