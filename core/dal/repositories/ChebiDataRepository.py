from eme.data_access import Repository, RepositoryBase
from sqlalchemy import and_, func

from core.dal.entities.dbdata.ChEBIData import ChEBIData


@Repository(ChEBIData)
class ChebiDataRepository(RepositoryBase):

    def get_first(self):
        return self.session.query(ChEBIData).first()
