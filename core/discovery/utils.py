from core.dal.views.metabolites import MetaboliteView


def create_empty_record(n, cnames, cvectors=None):
    pass


# def filter_requested_attr(df: MetaboliteView):
#     chebi_id
#     kegg_id
#     hmdb_id
#     lipidmaps_id
#     pubchem_id
#     cas_id
#     ref_etc
#     names
#     description
#     charge
#     mass
#     monoisotopic_mass
#     smiles
#     inchi
#     inchikey
#     formula


def guess_db(db_id: str):
    if db_id.startswith('HMDB'):
        return 'hmdb_id'
    elif db_id.startswith('CHEBI:'):
        return 'chebi_id'
    elif db_id.startswith('C'):
        return 'kegg_id'


def id_to_url(db_id, db_tag=None):
    if db_tag is None:
        db_tag = guess_db(db_id)
        if db_tag is None:
            return None

    # todo: if db_id lacks prefix, add it from db_tag

    url = None

    if db_tag == 'hmdb_id':
        url = f"https://hmdb.ca/metabolites/{db_id}"
    elif db_tag == 'chebi_id':
        url = f"https://www.ebi.ac.uk/chebi/searchId.do;?chebiId={db_id}"
    elif db_tag == 'kegg_id':
        url = f"https://www.genome.jp/dbget-bin/www_bget?cpd:{db_id}"
    elif db_tag == 'pubchem_id':
        url = f"https://pubchem.ncbi.nlm.nih.gov/compound/{db_id}"
    elif db_tag == 'lipidmaps_id':
        url = f"https://www.lipidmaps.org/data/LMSDRecord.php?LMID={db_id}"

    return url


def merge_attr(mv: MetaboliteView, attr, _val2):
    """
    merges _val2 into _val1

    :param mv: MetaboliteView to merge into
    :param attr: attribute name of MetaboliteView
    :param _val2: value to merge (can be list, set or tuple)
    """
    _val1 = getattr(mv, attr)

    if isinstance(_val1, set):
        if isinstance(_val2, (list, tuple, set)):
            _val1.update(_val2)
        else:
            _val1.add(_val2)
    elif isinstance(_val1, list):
        if isinstance(_val2, (list, tuple, set)):
            _val1.extend(_val2)
        else:
            _val1.append(_val2)
    else:
        if isinstance(_val2, (list, tuple, set)):
            raise Exception("Iterable provided for scalar value at MetaView merge!", attr, mv, _val2)

        setattr(mv, attr, _val2)
