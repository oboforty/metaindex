import random
import string
from typing import Sequence

from eme.data_access import get_repo

from core.dal import MetaboliteView, Metabolite
from core.discovery import resolve_single_id
from core.metabolite import get_metabolites, view_to_db
from modules.search import cache_search, search, SearchItem


_meta_repo = get_repo(Metabolite)


def search_metabolite(search_term, search_attr, discover: bool = True, cache: bool = True, verbose=True):

    result = search(search_term, attrs=[search_attr]).all()

    if not result:
        if discover:
            # search term is not cached. initiate discovery
            mv, resp = resolve_single_id(search_attr, search_term, verbose=verbose, cache=cache)

            if cache:
                # persist MetaView to Meta object
                meta = view_to_db(mv)

                # todo: @temporal:
                meta.meta_id = "".join(random.choices(string.ascii_uppercase, k=6))
                _meta_repo.create(meta)

                # cache approriate cache entry as well
                #cache_search([mv])

            # fake search, as it's either stored in DB or should be faked anyway
            sr = SearchItem(search_term=search_term, search_attr=search_attr)
            sr.search_attr, sr.entity_id = mv.search_endpoint
            result = [sr]

    return result


# @UNUSED:
def find_metabolite(search_term, search_attr, discover: bool = True, cache: bool = True) -> Sequence[MetaboliteView]:
    # todo: @later: also fetch all metabolites
    result = search(search_term, attrs=[search_attr])
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
