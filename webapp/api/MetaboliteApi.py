from modules.doors_oauth import require_oauth
from modules.eme_utils import ApiResponse

from core.dal import MetaboliteScalar, MetaboliteView


class MetaboliteApi:
    def __init__(self, server):
        self.route = '/api/metabolite'
        self.group = 'MetaboliteApi'

    @require_oauth('profile')
    def get(self):

        # Todo: later: how to rate limit anonymous user?

        return ApiResponse({

        })
