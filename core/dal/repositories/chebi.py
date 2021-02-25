from eme.data_access import Repository, RepositoryBase
from sqlalchemy import and_, func

from ..base.meta_repo import MetaboliteDataRepositoryBase
from ..entities.dbdata.chebi import ChEBIData


@Repository(ChEBIData)
class ChebiDataRepository(MetaboliteDataRepositoryBase):
    pass
