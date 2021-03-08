from modules.search.dal.entity import SearchItem

search_tables = {
    SearchItem
}

# and SEARCH_TYPES config file + service + CLI
def init_search(app, conf):

    pass
from sqlalchemy import and_, func

from core.dal.ctx import get_session
#from .entity import SearchItem

sess = None


def init_qb():
    global sess

    sess = get_session()


def search(search_type):

    # todo: itt:    how to cache non-id attrs, when they're not present in Metabolite?
    # todo:         if we do store them in Metabolite, that's redundant!
    # todo:         ... and the eme-search is pointless to exist
    # todo:         but if we don't, then we can't configure search as easily
    # todo:         ---> make custom search code and fuck eme module?
    # todo  -----------------> then put this logic into DAL <-------------------

    # names
    # description
    # charge
    # mass
    # monoisotopic_mass
    # smiles
    # inchi
    # inchikey
    # formula

    q = sess.query(SearchItem)\
        .filter(SearchItem.entity_type)
        .all()
