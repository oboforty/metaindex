from flask import request

from modules.doors_oauth import require_oauth
from modules.eme_utils import ApiResponse

from core.metabolite import search_metabolite
from modules.search import SearchItem


class SearchApi:
    def __init__(self, server):
        self.route = '/api/search'
        self.group = 'SearchApi'

        self.debug = server.debug

    #@require_oauth('profile')
    def get(self):
        search_term = request.args['s']
        search_attr = request.args.get('attr', None)

        if search_attr == 'all':
            search_attr = None
        else:
            search_attr = search_attr.split("|")

        # todo: add to settings
        discover = False
        discover_cache = False

        results = search_metabolite(search_term, search_attr, cache=discover_cache, discover=discover, verbose=self.debug)

        # todo: inchi & inchikey at once?

        # Todo: later: how to rate limit anonymous user?

        # results = [
        #     SearchItem(
        #         search_attr="names",
        #         search_term="ascorbic acid",
        #
        #         entity_id="AAAA",
        #         endpoint="/metabolite/AAAA",
        #         display="C-vitamin"
        #     ),
        #     SearchItem(
        #         search_attr="names",
        #         search_term="ascorbate",
        #
        #         entity_id="DDDD",
        #         endpoint="/metabolite/DDDD",
        #         display="Ascorbate"
        #     )
        # ]

        return ApiResponse([s.view for s in results])


    def get_molsearch(self):
        # todo: mol based search @later

        pass
