
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

