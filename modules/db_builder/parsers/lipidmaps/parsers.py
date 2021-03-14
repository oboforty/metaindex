import json

from core.dal.entities.dbdata.lipidmaps import LipidMapsData
from modules.db_builder.parsers.lib import strip_attr, force_list, flatten_refs, force_flatten_extra_refs
from modules.db_builder.parsers.pubchem.utils import split_pubchem_ids

_mapping = dict(
    LM_ID='lipidmaps_id',
    NAME='names',
    SYSTEMATIC_NAME='names',
    SYNONYMS='names',
    ABBREVIATION='names',

    EXACT_MASS='mass',
    #SMILES='smiles',
    #INCHI='inchi',
    INCHI_KEY='inchikey',
    #FORMULA='formula',

    #KEGG_ID='kegg_id',
    #HMDB_ID='hmdb_id',
    #CHEBI_ID='chebi_id',
    PUBCHEM_CID='pubchem_id',
    pubchem_compound_id='pubchem_id',
    #LIPIDBANK_ID='lipidbank_id',
    #SWISSLIPIDS_ID='swisslipids_id',

    wikipedia_id='wiki_id',

    #CATEGORY='category',
    #MAIN_CLASS='main_class',
    #SUB_CLASS='sub_class',
    CLASS_LEVEL4='lvl4_class',
)


def metajson_transform(me):
    flatten_refs(me)

    strip_attr(me, 'chebi_id', 'CHEBI:')
    strip_attr(me, 'chebi_id_alt', 'CHEBI:')
    strip_attr(me, 'hmdb_id', 'HMDB')
    strip_attr(me, 'lipidmaps_id', 'LM')
    strip_attr(me, 'inchi', 'InChI=')

    force_list(me, 'chebi_id_alt')
    force_list(me, 'names')

    split_pubchem_ids(me)

    force_flatten_extra_refs(me)


def parse_lipidmaps(content):
    if isinstance(content, str):
        data = json.loads(content)
    else:
        data = content

    for k in list(data.keys()):
        k2 = _mapping.get(k, k).lower()

        if k2 not in data:
            data[k2] = []

        v = data.pop(k)
        if isinstance(v, (list, tuple, set)):
            data[k2].extend(v)
        else:
            data[k2].append(v)

    # reduce vectors to scalars:
    metajson_transform(data)

    return LipidMapsData(**data)
