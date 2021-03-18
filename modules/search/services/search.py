from eme.data_access import get_repo
from sqlalchemy import and_, or_, distinct
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


def search(category: str, search_term: str, attrs: list = None):
    _search_strat: dict = _searches[category]
    if attrs is None:
        attrs = _search_strat.keys()

    is_distinct: bool = _search_strat['__distinct__']
    limit: int = _search_strat.get('__limit__', None)

    attr_classes = {
        'exact': [],
        'substring': [],
        'levenshtein': [],
        'approximate': []
    }

    for attr in attrs:
        if attr.startswith('__'): continue

        strat = _search_strat[attr] if attr in _search_strat else 'exact'
        attr_classes[strat].append(attr)

    # construct query
    _or_expr = []

    # exact match
    if attr_classes['exact']:
        _or_expr.append(and_(SearchItem.search_term == search_term, _match_sattr(attr_classes['exact'])))
    # like - substring
    if attr_classes['substring']:
        _or_expr.append(and_(SearchItem.search_term.like(f'%{search_term}%'), _match_sattr(attr_classes['substring'])))
    # if attr_classes['levenshtein']:
    #     _or_expr.append(and_(SearchItem.search_term == search_term, _match_sattr(attr_classes['levenshtein'])))
    # if attr_classes['approximate']:
    #     _or_expr.append(and_(SearchItem.search_term == search_term, _match_sattr(attr_classes['approximate'])))

    if not _or_expr:
        # todo error?
        return None

    session = _repo.session
    q = session.query(SearchItem)
    if is_distinct:
        # filter one entity per multiple attr match
        q = q.distinct(SearchItem.endpoint)

    if len(_or_expr) == 1:
        q = q.filter(_or_expr[0])
    else:
        q = q.filter(or_(*_or_expr))

    if limit:
        q = q.limit(limit)

    # query & return
    res = q.all()
    #print(res)
    return res


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


def _match_sattr(rr):
    if len(rr) > 1:
        return SearchItem.search_attr.in_(rr)
    else:
        return SearchItem.search_attr == rr[0]
