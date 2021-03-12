from core.dal import MetaboliteView
from core.discovery import resolve_single_id, resolve_metabolites
from core.metabolite import search_metabolite

class SearchCommand:

    def __init__(self, cli):
        self.cli = cli
        self.conf = cli.conf

    def run(self, search_term, discover: bool = False, cache: bool = False, search_attrs: list = None):
        # e.g.:
        # 6716 --discover=true --cache=true inchi inchikey
        search_metabolite(search_term, search_attrs, discover=discover, cache=cache)
