from .eme_utils import __module__ as utils
from .search import __module__ as search
from .db_builder import __module__ as db_builder
from .doors_oauth import __module__ as oauth
from .admin import __module__ as admin
from .comments import __module__ as comments
# favourites


modules = [
    utils,
    oauth,

    # todo:     unfinished eme modules
    search,
    comments,
    # favourites,

    db_builder,
    admin,
]
