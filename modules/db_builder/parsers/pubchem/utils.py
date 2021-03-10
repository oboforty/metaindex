
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
