import requests
from eme.data_access import get_repo

from modules.db_builder import parse_kegg
from .ManagerBase import ManagerBase
from core.dal import KeggData
from ..utils import pad_id


class KeggManager(ManagerBase):
    def __init__(self, dbconf):
        self.name = 'kegg'
        self.repo = get_repo(KeggData)
        self.conf = dbconf

        self._select = (
            'kegg_id', 'chebi_id', 'lipidmaps_id',
            'names', 'formula',
            'mass', 'monoisotopic_mass',
            #'comments'
        )

        self._reverse = (
            'chebi_id',
            'lipidmaps_id',
            #'pubchem_id'
        )

    def fetch_api(self, db_id, meta_view=True):
        r = requests.get(url=f'http://rest.kegg.jp/get/cpd:{pad_id(db_id, "kegg_id")}')

        data = parse_kegg(db_id, r.text)

        return self.to_view(data) if meta_view else data
