

def process_general_attributes(r, flavor: str):
    """
    Handles processing and trimming of general metabolite attributes
    """

    if flavor == 'hmdb':
        flatten_hmdb_hierarchies(r)

        for k, v in r.items():

            # todo: process extra refs?
            r[k] = flatten_list(v)

    strip_attr(r, 'chebi_id', 'CHEBI:')
    strip_attr(r, 'chebi_id_alt', 'CHEBI:')
    strip_attr(r, 'hmdb_id', 'HMDB')
    strip_attr(r, 'lipidmaps_id', 'LM')
    strip_attr(r, 'inchi', 'InChI=')

    force_list(r, 'chebi_id_alt')
    force_list(r, 'names')

    if flavor == 'chebi':
        # pubchem requires special attention

        # TODO: split pubchem SID not just ignore it!
        split_pubchem_ids(r)

        process_extra_refs(r, [
            'chebi_id_alt',
            'hmdb_id', 'pubchem_id', 'lipidmaps_id', 'kegg_id', 'cas_id',
            'chemspider_id', 'pubchem_sub_id', 'chembl_id', 'metabolights_id', 'swisslipids_id',
            'pdb_id', 'uniprot_id',
            'drugbank_id', 'kegg_drug_id',
            'wiki_id',
            # 'pubmed_id',
        ])


def process_extra_refs(r, attr_arr, ex_attr=None):
    if ex_attr is None:
        ex_attr = 'ref_etc'

    ref = r.setdefault(ex_attr, {})

    for attr in attr_arr:
        if attr not in r:
            continue

        val = r[attr]

        if isinstance(val, list) and len(val) > 1:
            r[attr] = val[0]
            ref.setdefault(attr, [])
            ref[attr].extend(val[1:])


def split_pubchem_ids(r):
    if 'pubchem_id' in r:
        p = r['pubchem_id']
        if isinstance(p, list):
            p = list(map(lambda p: p[5:], filter(lambda p: p.startswith('CID:'), p)))

            if len(p) > 1:
                pass
            elif len(p) == 0:
                del r['pubchem_id']
            else:
                # after filtering pubchem_id becomes scalar:
                p = p[0]

        r['pubchem_id'] = p


def flatten_hmdb_hierarchies(r):
    if 'synonyms' in r:
        synsyn = r.pop('synonyms')

        if synsyn and synsyn[0]:
            r['names'].extend(synsyn[0]['synonym'])
    elif 'names' in r:
        for i,syn in enumerate(r['names']):
            if isinstance(syn, dict):
                r['names'][i] = syn['synonym']

    if 'secondary_accessions' in r:
        accacc = r.pop('secondary_accessions')

        if accacc and accacc[0]:
            r['hmdb_id_alt'].extend(accacc[0]['accession'])
    elif 'hmdb_id_alt' in r:
        for i, syn in enumerate(r['hmdb_id_alt']):
            if isinstance(syn, dict):
                r['hmdb_id_alt'][i] = syn['accession']


# def pp(val, parse=None):
#     if parse is None:
#         return val
#     if val is None:
#         return None
#     return parse(val)


def force_list(r, key, f=None):
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


def flatten_list(v):
    if isinstance(v, list) and len(v) == 1:
        return v[0]
    else:
        return v


def strip_attr(r, key, prefix):
    if key not in r or not r[key]:
        return

    if isinstance(r[key], list):
        r[key] = list(map(lambda v: v.lstrip(prefix), r[key]))
    else:
        r[key] = r[key].lstrip(prefix)


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
