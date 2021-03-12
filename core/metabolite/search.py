from core.dal import MetaboliteView
from core.discovery import resolve_single_id
from core.metabolite import get_metabolites
from modules.search import cache_search, search, SearchItem


def search_metabolite(search_term, search_attr, discover: bool = True, cache: bool = True, verbose=True):

    result = search(search_term, attrs=[search_attr]).all()

    if not result:
        if discover:
            # search term is not cached. initiate discovery
            mv, resp = resolve_single_id(search_attr, search_term, verbose=verbose, cache=cache)

            # transform mv to search
            if cache:
                cache_search([mv])

            # fake search, as it's either stored in DB or should be faked anyway
            sr = SearchItem(search_term=search_term, search_attr=search_attr)
            sr.search_attr, sr.entity_id = mv.search_endpoint
            result = [sr]

    return result


def find_metabolite(search_term, search_attr, discover: bool = True, cache: bool = True):
    # todo: @later: also fetch all metabolites
    result = search(search_term, attrs=[search_attr])

    if not result:
        if discover:
            # search term is not cached. initiate discovery
            df: MetaboliteView = resolve_single_id(search_attr, search_term)
    else:
        # turn search result to metaview
        meta_ids = [sr.entity_id for sr in result]

        metas = get_metabolites(meta_ids)

    return metas
