

class ScanCommand:

    def __init__(self, cli):
        self.cli = cli

        self.scanners = {}

    def run(self):

        for name, xpl in self.scanners.items():
            print(f"Scanning {name}")
            xpl.run()
