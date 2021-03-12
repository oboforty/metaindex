import requests
from eme.data_access import get_repo

from .ManagerBase import ManagerBase
from core.dal import LipidMapsData
from ..utils import pad_id
from modules.db_builder import parse_lipidmaps


class LipidMapsManager(ManagerBase):
    def __init__(self, dbconf):
        self.name = 'lipidmaps'
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

    def fetch_api(self, db_id, meta_view=True):
        url = f'https://www.lipidmaps.org/rest/compound/lm_id/{pad_id(db_id, "lipidmaps_id")}/all/'
        r = requests.get(url=url)

        data = parse_lipidmaps(db_id, r.text)

        return self.to_view(data) if meta_view else data
