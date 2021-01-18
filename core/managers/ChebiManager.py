from eme.data_access import get_repo

from core.dal.entities.dbdata.ChEBIData import ChEBIData
from core.managers.ManagerBase import ManagerBase


class ChebiManager(ManagerBase):
    def __init__(self):
        self.name = 'chebi'
        self.repo = get_repo(ChEBIData)

        # todo: itt: mapping
        # todo: itt: api mapping - how?

    def fetch_api(self, db_id):
        pass

    def query_primary(self, db_id):
        pass

    def query_reverse(self, db_id):
        pass
