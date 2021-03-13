from typing import Sequence

from eme.data_access import get_repo

from core.dal import Metabolite, MetaboliteView, ChEBIData, HMDBData, KeggData, LipidMapsData, PubChemData, MetaboliteRepository
from core.discovery import getdb, db_managers

_repo: MetaboliteRepository = get_repo(Metabolite)


def get_metabolite(meta_id) -> MetaboliteView:
    meta: Metabolite = _repo.get(meta_id)

    return to_view(meta)


def get_metabolites(meta_ids) -> Sequence[MetaboliteView]:
    if not isinstance(meta_ids, (list, tuple, set)):
        raise Exception("please provide a list")

    metas = _repo.list(meta_ids)
    views = []

    for meta in metas:
        views.append(to_view(meta))

    return views


def to_view(meta: Metabolite):
    """
    Converts Metabolite db data entity to MetaboliteView
    """

    # todo: how to determine meta_id
    # todo: create a new service for it? :thonk:
    mv = MetaboliteView()

    _query_into_view(mv, 'chebi', meta.chebi_ids)
    _query_into_view(mv, 'hmdb', meta.hmdb_ids)
    _query_into_view(mv, 'pubchem', meta.pubchem_ids)
    _query_into_view(mv, 'kegg', meta.kegg_ids)
    _query_into_view(mv, 'lipidmaps', meta.lipidmaps_ids)

    return mv


def view_to_db(mv: MetaboliteView, resolve_from_db=False) -> Metabolite:
    if resolve_from_db:
        raise Exception("NOT IMPLEMENTED")

    meta = Metabolite()

    meta.chebi_ids = list(mv.chebi_id)
    meta.hmdb_ids = list(mv.hmdb_id)
    meta.pubchem_ids = list(mv.pubchem_id)
    meta.kegg_ids = list(mv.kegg_id)
    meta.lipidmaps_ids = list(mv.lipidmaps_id)
    meta.cas_ids = list(mv.cas_id)

    return meta


def _query_into_view(mv: MetaboliteView, db_tag, _ids):
    """
    Queries db_tag ids and adds them to the metabolite view
    """
    hand = getdb(db_tag)
    db_datas = hand.query_multiple(_ids)

    for db_data in db_datas:
        hand.merge_into(mv, db_data)
