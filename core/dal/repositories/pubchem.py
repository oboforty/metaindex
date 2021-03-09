from eme.data_access import Repository, RepositoryBase

from ..base.meta_repo import MetaboliteDataRepositoryBase
from ..entities.dbdata.pubchem import PubChemData


@Repository(PubChemData)
class PubChemDataRepository(MetaboliteDataRepositoryBase):
    primary_id = 'pubchem_id'
