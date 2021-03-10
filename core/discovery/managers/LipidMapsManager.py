from eme.data_access import get_repo

from .ManagerBase import ManagerBase
from core.dal import LipidMapsData
from core.discovery.utils import pad_id


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

        # todo : json parse
        #return self.to_view(data) if meta_view else data
