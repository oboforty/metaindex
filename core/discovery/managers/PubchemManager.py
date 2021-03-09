import requests
from eme.data_access import get_repo

from .ManagerBase import ManagerBase
from core.dal import PubChemData
from core.parsers import parse_pubchem


class PubchemManager(ManagerBase):
    def __init__(self, dbconf):
        self.name = 'pubchem'
        self.repo = get_repo(PubChemData)
        self.conf = dbconf

        self._select = (
            'pubchem_id', 'chebi_id', 'kegg_id', 'hmdb_id',
            'smiles', 'inchi', 'inchikey', 'formula', 'names',
            'mass', 'monoisotopic_mass'
            #'logp'
        )

        self._remap = {
            'monoisotopic': 'monoisotopic_mass',
            'hmdb': 'hmdb_id'
        }

        self._reverse = (
            'chebi_id', 'hmdb_id', 'kegg_id'
        )

    def fetch_api(self, db_id, save_cached=True):
        r = requests.get(url=f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{db_id}/json')
        r2 = requests.get(url=f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{db_id}/xrefs/SourceName,RegistryID/JSON')

        s1 = r.status_code
        s2 = r2.status_code

        if (s1 != 200 and s1 != 304) or (s2 != 200 and s2 != 304):
            return None

        data = parse_pubchem(db_id, r.text, r2.text)

        if save_cached:
            self.repo.create(data)

        return self.to_view(data)
