from eme.data_access import get_repo

from .ManagerBase import ManagerBase
from ...dal.entities.dbdata.lipidmaps import LipidMapsData


class LipidMapsManager(ManagerBase):
    def __init__(self, dbconf):
        self.name = 'hmdb'
        self.repo = get_repo(LipidMapsData)
        self.conf = dbconf

        self.padding = 'LM'

        self._select = (
            'pubchem_id', 'chebi_id', 'kegg_id', 'hmdb_id', 'lipidmaps_id',
            'smiles', 'inchi', 'inchikey', 'formula', 'names',
            'mass'
        )

        self._reverse = (
            'pubchem_id', 'kegg_id', 'hmdb_id', 'chebi_id',
        )

    def fetch_api(self, db_id):
        print("TODO API")
        return None
