from io import StringIO, BytesIO
import xml.etree.ElementTree as ET

from core.dal import HMDBData
from modules.db_builder.parsers.fileparsing import parse_xml_recursive

from modules.db_builder.parsers.hmdb.utils import flatten_hmdb_hierarchies
from modules.db_builder.parsers.lib import strip_attr, force_list, force_flatten_extra_refs, flatten_refs
from modules.db_builder.parsers.pubchem.utils import split_pubchem_ids

_mapping = dict(
    accession='hmdb_id',
    ##- secondary_accessions.accession = 'hmdb_id_alt',

    name='names',
    iupac_name='names',
    traditional_iupac='names',
    ##- synonyms.synonym = 'names',

    # description = 'description',
    state='state',

    average_molecular_weight='mass',
    monisotopic_molecular_weight='monoisotopic_mass',
    avg_mol_weight='mass',
    monoisotopic_mol_weight='monoisotopic_mass',
    chemical_formula='formula',
    smiles='smiles',
    inchi='inchi',
    inchikey='inchikey',

    cas_registry_number='cas_id',
    pubchem_compound_id='pubchem_id',
    wikipedia_id='wiki_id',

    # chemspider_id = 'chemspider_id',
    # kegg_id = 'kegg_id',
    # metlin_id = 'metlin_id',
    # chebi_id = 'chebi_id',
    # pdb_id = 'pdb_id',
    # drugbank_id = 'drugbank_id',
)


def metajson_transform(me):
    # flattens multi-level HMDB specific XML attributes into a list
    flatten_hmdb_hierarchies(me)

    # flattens lists of len=1
    flatten_refs(me)

    strip_attr(me, 'chebi_id', 'CHEBI:')
    strip_attr(me, 'hmdb_id', 'HMDB')
    strip_attr(me, 'lipidmaps_id', 'LM')
    strip_attr(me, 'inchi', 'InChI=')

    force_list(me, 'names')

    #split_pubchem_ids(me)

    # flattens everything else that wasn't flattened before
    # (len>1 lists are processed into extra refs JSON attribute)
    force_flatten_extra_refs(me)


def parse_hmdb(data):
    metajson_transform(data)

    return HMDBData(**data)


def parse_hmdb_api(data):
    global _mapping
    if data is None:
        return None

    context = ET.iterparse(BytesIO(data), events=("start", "end"))
    context = iter(context)

    _xevt, xmeta = next(context)

    # todo: refactor this into a custom func within the module
    me = parse_xml_recursive(context, has_xmlns=False, _mapping=_mapping)

    if isinstance(me, str) or me is None:
        return None

    return parse_hmdb(me)
