

def process_general_attributes(r, flavor: str):
    """
    Handles processing and trimming of general metabolite attributes
    """

    if flavor == 'hmdb':
        flatten_hmdb_hierarchies(r)

        for k, v in r.items():
            r[k] = flatten_list(v)


    strip_attr(r, 'chebi_id', 'CHEBI:')
    strip_attr(r, 'chebi_id_alt', 'CHEBI:')
    strip_attr(r, 'hmdb_id', 'HMDB')
    strip_attr(r, 'inchi', 'InChI=')

    force_list(r, 'chebi_id_alt')

    if flavor == 'chebi':
        # pubchem requires special attention
        split_pubchem_ids(r)


def process_names(*args):
    names = []

    for syn in args:
        if syn:
            if isinstance(syn, str):
                names.append(syn)
            else:
                for sy in syn:
                    names.append(sy)
    return list(set(names))


def process_extra_refs(dc, value, attr, parse=None):

    if isinstance(value, list):
        if len(value) == 1:
            return pp(value[0], parse)
        elif len(value) == 0:
            return None
        else:
            # return None, because the rest of Ids area stored in a json
            dc[attr] = [pp(el, parse) for el in value]
            return None

    # scalar type:
    return pp(value, parse)


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


def pp(val, parse=None):
    if parse is None:
        return val
    if val is None:
        return None
    return parse(val)


def force_list(r, key, f=None):
    if key not in r:
        return

    v = r[key]

    if isinstance(v, list):
        if f is not None:
            r[key] = [f(e) for e in v]
        r[key] = v
    elif v is None:
        r[key] = None
    else:
        if f is not None:
            r[key] = [f(v)]
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


def append_or_create(r, key, val):
    if key in r:
        key[r]


def _nil(var):
    if not bool(var):
        return True
    # accounts for xml newlines, whitespace & etc
    s = var.strip().replace('\r', '').replace('\n', '')
    return not bool(s)
