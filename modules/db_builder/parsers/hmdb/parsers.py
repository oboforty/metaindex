from io import StringIO, BytesIO
import xml.etree.ElementTree as ET

from core.dal import HMDBData
from modules.db_builder.parsers.fileparsing import parse_xml_recursive

from modules.db_builder.parsers.hmdb.utils import flatten_hmdb_hierarchies
from modules.db_builder.parsers.lib import strip_attr, force_list, force_flatten_extra_refs, flatten_refs
from modules.db_builder.parsers.pubchem.utils import split_pubchem_ids

_mapping: dict


def init_mapping(_map):
    global _mapping
    _mapping = _map


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

    metajson_transform(me)

    return HMDBData(**me)