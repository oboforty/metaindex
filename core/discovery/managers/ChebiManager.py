from eme.data_access import get_repo

from core.dal import ChEBIData
from .ManagerBase import ManagerBase


class ChebiManager(ManagerBase):
    def __init__(self, dbconf):
        self.name = 'chebi'
        self.repo = get_repo(ChEBIData)
        self.conf = dbconf

        self.padding = 'CHEBI:'

        self._select = (
            'chebi_id', 'pubchem_id', 'kegg_id', 'hmdb_id', 'lipidmaps_id',
            'smiles', 'inchi', 'inchikey', 'formula', 'names',
            'mass', 'monoisotopic_mass'
        )

        self._reverse = (
            'pubchem_id', 'kegg_id', 'hmdb_id', 'lipidmaps_id',
        )

    def fetch_api(self, db_id):
        print("TODO API")
        return None
