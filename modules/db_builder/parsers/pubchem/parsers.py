import json
import re
from collections import defaultdict

from core.dal import PubChemData
from modules.db_builder.parsers.lib import strip_attr, force_list, force_flatten_extra_refs, flatten_refs
from modules.db_builder.parsers.pubchem.utils import split_pubchem_ids

_mapping: dict


def init_mapping(_map):
    global _mapping
    _mapping = _map


def metajson_transform(me):
    flatten_refs(me)

    strip_attr(me, 'chebi_id', 'CHEBI:')
    strip_attr(me, 'hmdb_id', 'HMDB')
    strip_attr(me, 'lipidmaps_id', 'LM')
    strip_attr(me, 'inchi', 'InChI=')

    force_list(me, 'names')

    #split_pubchem_ids(me)

    # force non-scalars into extra refs
    force_flatten_extra_refs(me)


def parse_pubchem(db_id, c0,c1):
    """
    Parses API response for PubChem

    :param db_id:
    :param c0:
    :param c1:
    :return:
    """

    data = defaultdict(list)
    _refs = defaultdict(list)

    content = json.loads(c0)
    cont_refs = json.loads(c1)

    # parse xrefs:
    INF = cont_refs['InformationList']['Information'][0]

    # todo: itt: smart guess IDs and insert
    for db_id in INF['RegistryID']:
        if db_id.startswith('CHEBI:'):
            db_tag = 'chebi_id'
        elif db_id.startswith('HMDB'):
            db_tag = 'hmdb'
        elif re.match('C\d{4,9}', db_id):
            db_tag = 'kegg_id'
        else:
            continue
        _refs[db_tag].append(db_id)
    #INF['SourceName']
    # for db_tag, db_id in zip(INF['SourceName'], INF['RegistryID']):
    #     db_tag = db_tag.lower()
    #
    #     if db_tag == 'human metabolome database (hmdb)':
    #         db_tag = 'hmdb'
    #
    #     _refs[db_tag].append(db_id)

    data.update(content['PC_Compounds'][0])
    props = data.pop('props')
    pubchem_id = data['id']['id']['cid']

    for prop in props:
        label = prop['urn']['label']

        if label == 'InChI':
            data['inchi'].append(prop['value']['sval'])
        elif label == 'InChIKey':
            data['inchikeys'].append(prop['value']['sval'])
        elif label == 'SMILES':
            data['smiles'].append(prop['value']['sval'])
        elif label == 'IUPAC Name':
            data['names'].append(prop['value']['sval'])
        elif label == 'Molecular Formula':
            data['formula'].append(prop['value']['sval'])
        # elif label == 'Mass':
        #     data['mass'].append(prop['value']['fval'])
        elif label == 'Molecular Weight':
            data['mass'].append(prop['value']['fval'])
        elif label == 'Weight' and prop['urn']['name'] == 'MonoIsotopic':
            data['monoisotopic'].append(prop['value']['fval'])
        elif label == 'Log P':
            data['logp'].append(prop['value']['fval'])
        else:
            data[label] = prop['value']

    # merge and transform to standard json
    data.update(_refs)
    metajson_transform(data)

    return PubChemData(pubchem_id=pubchem_id, **data)
