
const _PADDINGS = {
    'hmdb_id': 'HMDB',
    'chebi_id': 'CHEBI:',
    //'kegg_id': 'C',
    'lipidmaps_id': 'LM',
}


export function guess_db(db_id) {
    for (let [db_tag, _pad] of Object.items(_PADDINGS)) {
        if (db_id.startsWith(_pad)) {
            return db_tag;
        }
    }
}


export function id_to_url(db_id, db_tag) {
    var db_id = pad_id(db_id, db_tag);

    switch(db_tag) {
        case 'hmdb_id':
            return `https://hmdb.ca/metabolites/${db_id}`
        case 'chebi_id':
            return `https://www.ebi.ac.uk/chebi/searchId.do;?chebiId=${db_id}`
        case 'kegg_id':
            return `https://www.genome.jp/dbget-bin/www_bget?cpd:${db_id}`
        case 'pubchem_id':
            return `https://pubchem.ncbi.nlm.nih.gov/compound/${db_id}`
        case 'lipidmaps_id':
            return `https://www.lipidmaps.org/data/LMSDRecord.php?LMID=${db_id}`
    }
    
    return db_id;
}

export function depad_id(db_id, db_tag) {
    let padding = _PADDINGS[db_tag];

    if (padding && db_id.startsWith(padding))
        return db_id.substring(len(padding));

    return db_id;
}

export function pad_id(db_id, db_tag) {
    let padding = _PADDINGS[db_tag];

    if (!padding || db_id.startsWith(padding))
        return db_id;

    return padding+db_id;
}