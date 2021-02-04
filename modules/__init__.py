from modules import eme_utils
from modules import search
from modules import db_builder
from modules import doors_oauth
from modules import admin
from modules import comments
#from modules import favourites


modules = [
    eme_utils,
    doors_oauth,

    # todo:     unfinished eme modules
    search,
    comments,
    # favourites,

    db_builder,
    admin,
]
