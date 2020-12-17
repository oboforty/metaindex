from modules.db_builder.services.explore.hmdb_xml import parse_hmdb_xml


class HMDBXMLExplorer:

    def __init__(self, conf):
        self.path = conf['bulk_db']['base'] + conf['bulk_db']['hmdb_xml']

    def run(self):
        parse_hmdb_xml(self.path)
