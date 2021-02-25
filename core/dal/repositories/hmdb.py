from eme.data_access import Repository, RepositoryBase

from ..entities.dbdata.hmdb import HMDBData


@Repository(HMDBData)
class HMDBDataRepository(RepositoryBase):

    def get_first(self):
        return self.session.query(HMDBData).first()
