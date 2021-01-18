from eme.data_access import Repository, RepositoryBase
from sqlalchemy import and_, func

from core.dal.base.meta_repo import MetaboliteDataRepositoryBase
from core.dal.entities.dbdata.ChEBIData import ChEBIData


@Repository(ChEBIData)
class ChebiDataRepository(MetaboliteDataRepositoryBase):
    pass
