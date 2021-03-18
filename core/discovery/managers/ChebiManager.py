import requests
from eme.data_access import get_repo

from core.dal import ChEBIData
from modules.db_builder import parse_chebi_api
from .ManagerBase import ManagerBase
from ..utils import pad_id


class ChebiManager(ManagerBase):
    def __init__(self, dbconf):
        self.name = 'chebi'
        self.repo = get_repo(ChEBIData)
        self.conf = dbconf

        self.padding = 'CHEBI:'

        self._select = (
            'chebi_id', 'pubchem_id', 'kegg_id', 'hmdb_id', 'lipidmaps_id',
            'smiles', 'inchi', 'inchikey', 'formula', 'names',
            'mass', 'monoisotopic_mass',
            'ref_etc'
        )

        self._reverse = (
            'pubchem_id', 'kegg_id', 'hmdb_id', 'lipidmaps_id',
        )

    def fetch_api(self, db_id, meta_view=True):
        url = f'https://www.ebi.ac.uk/webservices/chebi/2.0/test/getCompleteEntity?chebiId={pad_id(db_id, "chebi_id")}'
        r = requests.get(url=url)

        data = parse_chebi_api(r.text)

        return self.to_view(data) if meta_view else data

