
_SPEC_REF_ATTR = (
    'chebi_id_alt', 'hmdb_id_alt',
    'hmdb_id', 'pubchem_id', 'lipidmaps_id', 'kegg_id', 'cas_id', 'chebi_id',
    'chemspider_id', 'pubchem_sub_id', 'chembl_id', 'metabolights_id', 'swisslipids_id',
    'pdb_id', 'uniprot_id',
    'drugbank_id', 'kegg_drug_id',
    'wiki_id',
    #'pubmed_id',

    'inchi', 'inchikey', 'smiles',
    'mass', 'monoisotopic_mass',"charge",
    'formula',
)


def rlen(v):
    if isinstance(v, list):
        return len(v)
    elif v is None:
        return 0
    else:
        return 1


def _nil(var):
    if not bool(var):
        return True
    # accounts for xml newlines, whitespace & etc
    s = var.strip().replace('\r', '').replace('\n', '')
    return not bool(s)


def strip_attr(r, key, prefix):
    if key not in r or not r[key]:
        return

    if isinstance(r[key], list):
        r[key] = list(map(lambda v: v.lstrip(prefix), r[key]))
    else:
        r[key] = r[key].lstrip(prefix)


def flatten(v, attr=None):
    """
    Flattens value
    """
    if attr is not None:
        if isinstance(v,dict) and attr in v:
            v[attr] = flatten(v[attr])
        return

    if isinstance(v, (list, tuple, set)) and len(v) == 1:
        return list(v)[0]
    else:
        return v


def force_list(r, key, f=None):
    """
    Forces value to be a list of element 1
    """
    if key not in r:
        return

    v = r[key]

    if isinstance(v, list):
        if f is not None:
            r[key] = [f(e) for e in v]
        else:
            r[key] = v
    elif v is None:
        r[key] = None
    else:
        if f is not None:
            r[key] = [f(v)]
        else:
            r[key] = [v]


def force_flatten_extra_refs(r, ex_attr=None):
    """
    Processes extra references (beyond the 1st value for scalars)
    and adds them to a json dictionary
    => thus keeping ref attributes flat scalar

    :param r:
    :param ex_attr:
    :return:
    """

    if ex_attr is None:
        ex_attr = 'ref_etc'

    ref = r.setdefault(ex_attr, {})

    for attr in _SPEC_REF_ATTR:
        if attr not in r:
            continue

        val = r[attr]

        if isinstance(val, (list, tuple, set)):
            if len(val) > 1:
                val = list(val)
                # forces scalar
                r[attr] = val[0]
                ref.setdefault(attr, [])
                ref[attr].extend(val[1:])

            else:
                # forces scalar anyway:
                r[attr] = flatten(r[attr])


def flatten_refs(r):
    """
    Flattens all ref attributes that have a length of 1
    """

    for attr in _SPEC_REF_ATTR:
        if attr not in r:
            continue
        r[attr] = flatten(r[attr])
