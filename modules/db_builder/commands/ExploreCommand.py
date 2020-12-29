

class ExploreCommand:

    def __init__(self, cli):
        self.cli = cli

        self.explorers = {}

    def run(self, db=None):
        if db is None:
            for name, xpl in self.explorers.items():
                print(f"Exploring {name}")
                xpl.run()
        else:
            self.explorers[db].run()
