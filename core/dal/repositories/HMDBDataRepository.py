from eme.data_access import Repository, RepositoryBase

from core.dal.entities.dbdata.HMDBData import HMDBData


@Repository(HMDBData)
class HMDBDataRepository(RepositoryBase):

    def get_first(self):
        return self.session.query(HMDBData).first()
