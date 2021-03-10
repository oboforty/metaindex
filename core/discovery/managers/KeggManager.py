import requests
from eme.data_access import get_repo

from modules.db_builder import parse_kegg
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
            #'comments'
        )

        self._remap = {
            "exact_mass": "monoisotopic_mass",
            "mol_weight": "mass"
        }

        self._reverse = (
            'chebi_id',
            'lipidmaps_id',
            #'pubchem_id'
        )

    def fetch_api(self, db_id, meta_view=True):
        r = requests.get(url=f'http://rest.kegg.jp/get/cpd:{db_id}')

        data = parse_kegg(db_id, r.text)

        return self.to_view(data) if meta_view else data
