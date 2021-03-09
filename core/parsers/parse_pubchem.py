import json
import re
from collections import defaultdict

from core.dal import PubChemData
from modules.db_builder import process_general_attributes


def parse_pubchem(db_id, c0,c1):
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

    process_general_attributes(data, flavor='pubchem')
    process_general_attributes(_refs, flavor='pubchem')

    q = _refs['ref_etc']
    p = data.pop('ref_etc')
    for k,v in p.items():
        q[k].append(v)

    return PubChemData(pubchem_id=pubchem_id, **data, **_refs)
