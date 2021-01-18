from eme.data_access import Repository, RepositoryBase
from sqlalchemy import and_, func

from core.dal.entities.dbdata.LipidMapsData import LipidMapsData


@Repository(LipidMapsData)
class LipidMapsDataRepository(RepositoryBase):

    def get_first(self):
        return self.session.query(LipidMapsData).first()
