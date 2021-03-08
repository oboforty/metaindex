from eme.data_access import get_repo

from .ManagerBase import ManagerBase
from ...dal.entities.dbdata.hmdb import HMDBData


class HmdbManager(ManagerBase):
    def __init__(self, dbconf):
        self.name = 'hmdb'
        self.repo = get_repo(HMDBData)
        self.conf = dbconf

        self.padding = 'HMDB'

        self._select = (
            'pubchem_id', 'chebi_id', 'kegg_id', 'hmdb_id', 'metlin_id',
            'smiles', 'inchi', 'inchikey', 'formula', 'names',
            'avg_mol_weight', 'monoisotopic_mol_weight'
        )

        self._remap = {
            'avg_mol_weight': 'mass',
            'monoisotopic_mol_weight': 'monoisotopic_mass'
        }

        self._reverse = (
            'pubchem_id', 'kegg_id', 'chebi_id',
        )

    def fetch_api(self, db_id):
        print("TODO API")
        return None
