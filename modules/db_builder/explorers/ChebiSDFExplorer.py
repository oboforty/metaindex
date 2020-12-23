from modules.db_builder.services.explore.chebi_sdf import parse_chebi_sdf


class ChebiSDFExplorer:

    def __init__(self, conf):
        self.path = conf['bulk_db']['base'] + conf['bulk_db']['chebi_sdf']

    def run(self):
        parse_chebi_sdf(self.path)
