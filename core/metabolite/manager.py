from eme.data_access import get_repo

from core.dal import Metabolite, MetaboliteView, ChEBIData, HMDBData, KeggData, LipidMapsData, PubChemData, MetaboliteRepository
from core.discovery import getdb, db_managers

_repo: MetaboliteRepository = get_repo(Metabolite)


def get_metabolite(meta_id) -> MetaboliteView:
    meta: Metabolite = _repo.get(meta_id)
    resolve_data_tables(meta)
    return meta


def get_metabolites(meta_ids) -> MetaboliteView:
    if not isinstance(meta_ids, (list, tuple, set)):
        raise Exception("please provide a list")

    metas = _repo.list(meta_ids)

    for meta in metas:
        resolve_data_tables(meta)
    return metas


def resolve_data_tables(meta: Metabolite):
    query_into_view(meta, 'chebi', meta.chebi_ids)
    query_into_view(meta, 'hmdb', meta.hmdb_ids)
    query_into_view(meta, 'pubchem', meta.pubchem_ids)
    query_into_view(meta, 'kegg', meta.kegg_ids)
    query_into_view(meta, 'lipidmaps', meta.lipidmaps_ids)


def query_into_view(meta: MetaboliteView, db_tag, _ids):
    """
    Queries db_tag ids and adds them to the metabolite view
    """
    hand = getdb(db_tag)
    db_datas = hand.query_multiple(_ids)

    for db_data in db_datas:
        hand.merge_into(meta, db_data)
