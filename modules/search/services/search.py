from sqlalchemy import and_, func
from core.dal.ctx import get_session

from ..dal.entity import SearchItem

"""
Add levensthein distance (EME?)
 https://towardsdatascience.com/fuzzy-matching-with-levenshtein-and-postgresql-ed66cad01c03

"""
_searches: dict


def init_search(app, conf):
    global _searches
    _searches = conf


def search(search: str, attrs: list = None):
    sess = get_session()

    q = sess.query(SearchItem)\
        .filter(SearchItem.search_term == search)

    if attrs:
        q = q.filter(SearchItem.search_attr.in_(attrs))

    # .all()
    return q


def cache_search(entities):
    global _searches
    sess = get_session()

    # todo: @temporal: no subents
    ent = entities[0]
    cfg = _searches[ent.search_entity]

    for attr in cfg['attributes']:
        st = SearchItem()
        st.search_attr = f'{ent.search_entity}.{attr}'
        st.search_term = getattr(ent, attr)
        st.endpoint, st.entity_id = ent.search_endpoint

        sess.add(st)

    sess.commit()


def clear_table():
    sess = get_session()

    sess.execute(f'TRUNCATE TABLE {SearchItem.__tablename__}')
    sess.commit()
