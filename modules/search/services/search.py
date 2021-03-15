from eme.data_access import get_repo
from sqlalchemy import and_, func
from core.dal.ctx import get_session

from ..dal.entity import SearchItem
from ..dal.repository import SearchItemRepository

"""
Add levensthein distance (EME?)
 https://towardsdatascience.com/fuzzy-matching-with-levenshtein-and-postgresql-ed66cad01c03

"""
_searches: dict
_repo: SearchItemRepository = get_repo(SearchItem)


def init_search(app, conf):
    global _searches, _repo
    _searches = conf
    _repo = get_repo(SearchItem)


def search(search: str, attrs: list = None):
    #global _repo
    return _repo.search(search, attrs)


def cache_search(entities):
    global _searches

    # todo: @temporal: no subents
    ent = entities[0]
    cfg = _searches[ent.search_entity]

    for attr in cfg['attributes']:
        st = SearchItem()
        st.search_attr = f'{ent.search_entity}.{attr}'
        st.search_term = getattr(ent, attr)
        st.endpoint, st.entity_id = ent.search_endpoint

        _repo.create(st, commit=False)
    _repo.save()



def clear_table():
    sess = get_session()

    sess.execute(f'TRUNCATE TABLE {SearchItem.__tablename__}')
    sess.commit()
