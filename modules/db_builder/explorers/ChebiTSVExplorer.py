from ..services.explore.chebi_tsv import parse_chebi_tsv


class ChebiTSVExplorer:

    def __init__(self, conf):
        self.path = conf['bulk_db']['base'] + conf['bulk_db']['chebi_tsv']

    def run(self):
        parse_chebi_tsv(self.path)
