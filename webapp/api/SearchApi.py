from flask import request

from modules.doors_oauth import require_oauth
from modules.eme_utils import ApiResponse

from core.metabolite import search_metabolite
from modules.search import SearchItem


class SearchApi:
    def __init__(self, server):
        self.route = '/api/search'
        self.group = 'SearchApi'

    #@require_oauth('profile')
    def get(self):
        search_term = request.args['s']
        search_attr = request.args['attr']

        # todo: inchi & inchikey at once?

        # Todo: later: how to rate limit anonymous user?

        results = [
            SearchItem(
                search_attr="names",
                search_term="ascorbic acid",

                entity_id="AAAA",
                endpoint="/metabolite/AAAA",
                display="C-vitamin"
            ),
            SearchItem(
                search_attr="names",
                search_term="ascorbate",

                entity_id="DDDD",
                endpoint="/metabolite/DDDD",
                display="Ascorbate"
            )
        ]

        return ApiResponse([s.view for s in results])


    def get_molsearch(self):
        # todo: mol based search @later

        pass
