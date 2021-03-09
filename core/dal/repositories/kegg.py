from eme.data_access import Repository, RepositoryBase

from ..base.meta_repo import MetaboliteDataRepositoryBase
from ..entities.dbdata.kegg import KeggData


@Repository(KeggData)
class KeggDataRepository(MetaboliteDataRepositoryBase):
    primary_id = 'kegg_id'
