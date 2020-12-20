

class InsertCommand:

    def __init__(self, cli):
        self.cli = cli
        self.inserters = {}

    def run(self, db: str, autoclear: bool = False):
        self.inserters[db.title()].run(autoclear=autoclear)
