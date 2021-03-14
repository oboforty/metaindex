from modules.doors_oauth import require_oauth
from modules.eme_utils import ApiResponse

from core.dal import MetaboliteScalar


class DiscoveryApi:
    def __init__(self, server):
        self.route = '/api/metabolite'
        self.group = 'DiscoveryApi'

    @require_oauth('profile')
    def get_discover(self):
        # todo: discover from DF
        # todo: discover from db_tag,db_id

        # Todo: later: how to rate limit anonymous user?

        return ApiResponse({

        })
