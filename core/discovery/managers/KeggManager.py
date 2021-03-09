from eme.data_access import get_repo

from .ManagerBase import ManagerBase
from core.dal import KeggData


class KeggManager(ManagerBase):
    def __init__(self, dbconf):
        self.name = 'kegg'
        self.repo = get_repo(KeggData)
        self.conf = dbconf

        self._select = (
            'kegg_id', 'chebi_id', 'lipidmaps_id',
            'names', 'formula',
            'exact_mass', 'mol_weight',
            'comments'
        )

        self._reverse = (
            'chebi_id',
            'lipidmaps_id',
            #'pubchem_id'
        )

    def fetch_api(self, db_id):
        print("TODO API")
        return None
