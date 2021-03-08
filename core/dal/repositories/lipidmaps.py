from eme.data_access import Repository, RepositoryBase
from sqlalchemy import and_, func

from ..base.meta_repo import MetaboliteDataRepositoryBase
from ..entities.dbdata.lipidmaps import LipidMapsData


@Repository(LipidMapsData)
class LipidMapsDataRepository(MetaboliteDataRepositoryBase):
    primary_id = 'lipidmaps_id'