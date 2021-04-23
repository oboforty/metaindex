import random
import string
from typing import Sequence

from eme.data_access import get_repo

from core.dal import MetaboliteView, Metabolite
from core.discovery import resolve_single_id
from core.metabolite import get_metabolites, view_to_db
from modules.search import search, SearchItem

_meta_repo = get_repo(Metabolite)

_ENDPOINT = '/metabolite/{}'


def search_metabolite(search_term, search_attr: list, discover: bool = True, cache: bool = True, verbose=True):
    if not isinstance(search_attr, (list, tuple, set)) and search_attr is not None:
        search_attr = [search_attr]

    result = search('metabolite', search_term, attrs=search_attr)

    if not result and discover:
        # search term is not cached. initiate discovery
        mv, resp = resolve_single_id(search_attr, search_term, verbose=verbose, cache=cache)

        if cache:
            # persist MetaView to Meta object
            meta = view_to_db(mv)

            # todo: @temporal id
            mv.meta_id = "".join(random.choices(string.ascii_uppercase, k=6))
            meta.meta_id = mv.meta_id
            _meta_repo.create(meta)

            # cache approriate cache entry as well
            sr = cache_search_metabolite(mv, search_attr)
        #else:
        # fake search, as it's either stored in DB or should be faked anyway
        sr = SearchItem(search_term=search_term, search_attr=search_attr)
        sr.endpoint, sr.entity_id = mv.search_endpoint

        result = [sr]

    return result


def cache_search_metabolite(mv: MetaboliteView, attrs=None) -> SearchItem:
    _requested_search_item = None
    _repo = get_repo(SearchItem)

    endpoint = _ENDPOINT.format(mv.meta_id)
    display = mv.primary_name

    # Todo: ITT: make names lowercase set everywhere

    for db_tag, db_ids in mv.refs:
        for db_id in db_ids:
            _repo.create(
                SearchItem(search_term=db_id, search_attr=db_tag, entity_id=mv.meta_id, endpoint=endpoint, display=display),
                commit=False)

    for attr, values in mv.attributes:
        for value in values:
            _repo.create(
                SearchItem(search_term=value, search_attr=attr, entity_id=mv.meta_id, endpoint=endpoint, display=display),
                commit=False)

    _repo.save()

    #return _requested_search_item


# @UNUSED:
def find_metabolite(search_term, search_attr, discover: bool = True, cache: bool = True) -> Sequence[MetaboliteView]:
    # todo: @later: also fetch all metabolites
    result = search('metabolite', search_term, attrs=[search_attr])
    metas = []

    if not result:
        if discover:
            # search term is not cached. initiate discovery
            df: MetaboliteView = resolve_single_id(search_attr, search_term)
            metas.append(df)
    else:
        # turn search result to metaview
        meta_ids = [sr.entity_id for sr in result]

        metas = get_metabolites(meta_ids)

    return metas
