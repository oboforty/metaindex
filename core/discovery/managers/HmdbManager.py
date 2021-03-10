import requests
from eme.data_access import get_repo

from core.dal import HMDBData
from core.discovery.utils import pad_id
from modules.db_builder import parse_hmdb

from .ManagerBase import ManagerBase


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

    def fetch_api(self, db_id, meta_view=True):
        db_id = pad_id(db_id, 'hmdb_id')
        r = requests.get(url=f'http://www.hmdb.ca/metabolites/{db_id}.xml')

        if r.status_code != 200 and r.status_code != 304:
            return None

        data: HMDBData = parse_hmdb(r.content)

        return self.to_view(data) if meta_view else data
