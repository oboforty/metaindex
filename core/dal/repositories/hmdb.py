from eme.data_access import Repository, RepositoryBase

from ..base.meta_repo import MetaboliteDataRepositoryBase
from ..entities.dbdata.hmdb import HMDBData


@Repository(HMDBData)
class HMDBDataRepository(MetaboliteDataRepositoryBase):
    primary_id = 'hmdb_id'
