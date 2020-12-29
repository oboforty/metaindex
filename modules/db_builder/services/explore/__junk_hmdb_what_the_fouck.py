if isinstance(me['secondary_accessions'], str):
    idmap[me['secondary_accessions']] = me['accession']
    N_secondary += 1

    if not (len(me['secondary_accessions']) == 9 and me['secondary_accessions'][4:] == me['accession'][6:]):
        has_secondary = True
elif me['secondary_accessions']['accession']:
    if isinstance(me['secondary_accessions']['accession'], str):
        N_secondary += 1
        idmap[me['secondary_accessions']['accession']] = me['accession']

        if not (len(me['secondary_accessions']['accession']) == 9 and me['secondary_accessions']['accession'][4:] == me[
                                                                                                                         'accession'][
                                                                                                                     6:]):
            has_secondary = True

    else:
        for sec in me['secondary_accessions']['accession']:
            idmap[sec] = me['accession']
            N_secondary += 1

            if not (len(sec) == 9 and sec[4:] == me['accession'][6:]):
                has_secondary = True
