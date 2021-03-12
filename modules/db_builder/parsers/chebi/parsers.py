from collections import defaultdict
import requests
import xmltodict

from ..lib import strip_attr, force_list, flatten_refs, force_flatten_extra_refs
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

    split_pubchem_ids(me)

    force_flatten_extra_refs(me)


def parse_chebi(db_id, content):
    refs = defaultdict(list)

    cont = dict(xmltodict.parse(content))
    x = cont['S:Envelope']['S:Body']['getCompleteEntityResponse']['return']

    # add DatabaseLinks as refs
    for oof in x.pop('DatabaseLinks'):
        db_tag = oof['type'].lower()
        db_id = oof['data']

        if 'kegg' in db_tag:
            refs['kegg'].append(db_id)
        else:
            refs[db_tag].append(db_id)

    # todo: add data from x
    data = dict(x)
    names = [x.get('chebiAsciiName')]

    return data, refs
