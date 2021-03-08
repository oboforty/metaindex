from eme.data_access import Repository, RepositoryBase
from sqlalchemy import and_, func

from ..base.meta_repo import MetaboliteDataRepositoryBase
from ..entities.dbdata.chebi import ChEBIData


@Repository(ChEBIData)
class ChebiDataRepository(MetaboliteDataRepositoryBase):
    primary_id = 'chebi_id'

    # def get(self, db_id):
    #     return self.session.query(
    #         C.pubchem_id, C.chebi_id, C.kegg_id, C.hmdb_id, C.lipidmaps_id,
    #         C.smiles, C.inchi, C.inchikey, C.formula, C.names,
    #         C.mass, C.monoisotopic_mass
    #     )\
    #         .filter(C.chebi_id == db_id)\
    #         .first()

