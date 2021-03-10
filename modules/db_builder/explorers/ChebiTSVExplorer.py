from modules.db_builder.parsers.chebi.tsv_expl import explore_chebi_tsv


class ChebiTSVExplorer:

    def __init__(self, conf):
        self.path = conf['base'] + conf['chebi_tsv']

    def run(self):
        explore_chebi_tsv(self.path)
