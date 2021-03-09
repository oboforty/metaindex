from core.dal.views.metabolites import MetaboliteView


def gecc(mv: MetaboliteView):

    str0 = []

    if mv.chebi_id is not None: str0.append(mv.chebi_id)
    if mv.hmdb_id is not None: str0.append(mv.hmdb_id)
    if mv.lipidmaps_id is not None: str0.append(mv.lipidmaps_id)
    if mv.cas_id is not None: str0.append(mv.cas_id)
    if mv.metlin_id is not None: str0.append(mv.metlin_id)
    if mv.kegg_id is not None: str0.append(mv.kegg_id)
    if mv.pubchem_id is not None: str0.append(mv.pubchem_id)
    if mv.ref_etc: str0.append("extra_refs")

    return ",".join(str0)
