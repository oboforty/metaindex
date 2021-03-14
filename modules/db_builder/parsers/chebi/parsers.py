import json
from collections import defaultdict
import requests
import xmltodict

from core.dal import ChEBIData
from ..lib import strip_attr, force_list, flatten_refs, force_flatten_extra_refs, flatten
from .utils import flatten_chebi_api_attr
from ..pubchem.utils import split_pubchem_ids

# Chebi Bulk DB mapping
_mapping = {
  'ChEBI ID': 'chebi_id',
  'Secondary ChEBI ID': 'chebi_id_alt',

  'ChEBI Name': 'names',
  'IUPAC Names': 'names',
  'Synonyms': 'names',

  'Formulae': 'formula',
  'InChI': 'inchi',
  'InChIKey': 'inchikey',
  'SMILES': 'smiles',

  'Definition': 'description',
  'PubChem Database Links': 'pubchem_id',
  'KEGG COMPOUND Database Links': 'kegg_id',
  'HMDB Database Links': 'hmdb_id',
  'LIPID MAPS instance Database Links': 'lipidmaps_id',
  'LIPID MAPS class Database Links': 'lipidmaps_class_id',
  'CAS Registry Numbers': 'cas_id',
  'Chemspider Database Links': 'chemspider_id',

  'PubMed citation Links': 'pubmed_id',
  'PDB Database Links': 'pdb_id',
  'UniProt Database Links': 'uniprot_id',
  'SwissLipids Database Links': 'swisslipids_id',
  'Wikipedia Database Links': 'wiki_id',
  'DrugBank Database Links': 'drugbank_id',

  'Star': 'quality',
  'Charge': 'charge',
  'Mass': 'mass',
  'Monoisotopic Mass': 'monoisotopic_mass',
}

# chebi API XML mapping
_mapping_api = {
    'chebiId': 'chebi_id',

    'chebiAsciiName': 'names',
    'Synonyms': 'names',
    'IupacNames': 'names',

    #'definition': '',
    #'status': '',
    # 'smiles': '',
    # 'inchi': '',
    # 'inchiKey': '',
    #'charge': '',
    #'mass': '',
    'monoisotopicMass': 'monoisotopic_mass',

    'entityStar': 'stars',
    'Formulae': 'formula',
    # 'RegistryNumbers': '',
    # 'Citations': '',
    # 'ChemicalStructures': '',
    # 'DatabaseLinks': '',
    # 'OntologyParents': '',
    # 'OntologyChildren': '',
    # 'CompoundOrigins': ''
}


def metajson_transform(me):
    flatten_refs(me)

    strip_attr(me, 'chebi_id', 'CHEBI:')
    strip_attr(me, 'chebi_id_alt', 'CHEBI:')
    strip_attr(me, 'hmdb_id', 'HMDB')
    strip_attr(me, 'lipidmaps_id', 'LM')
    strip_attr(me, 'inchi', 'InChI=')

    force_list(me, 'chebi_id_alt')
    force_list(me, 'names')

    flatten(me, 'quality')
    flatten(me, 'description')

    split_pubchem_ids(me)


    force_flatten_extra_refs(me)

def parse_chebi(content):
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


    metajson_transform(data)

    return ChEBIData(**data)


def parse_chebi_api(content):
    refs = defaultdict(list)

    cont = xmltodict.parse(content)
    ch = cont['S:Envelope']['S:Body']['getCompleteEntityResponse']['return']

    # add DatabaseLinks as refs
    for oof in ch.pop('DatabaseLinks'):
        db_tag = oof['type'].lower()
        db_tag = _mapping_api.get(db_tag, db_tag)
        db_id = oof['data']

        refs[db_tag].append(db_id)

    for state in list(ch.keys()):
        flatten_chebi_api_attr(ch, state, _mapping=_mapping_api)
    ch.update(refs)
    metajson_transform(ch)

    return ChEBIData(**ch)
