from io import StringIO, BytesIO
import xml.etree.ElementTree as ET

from core.dal import HMDBData
from modules.db_builder.services.fileparsing import parse_xml_recursive
from modules.db_builder.services.attr_parsing import process_general_attributes

from modules.db_builder.__module__ import conf
_mapping = conf.get('mapping_hmdb')


def parse_hmdb_str_xml(data):
    if data is None:
        return None

    context = ET.iterparse(BytesIO(data), events=("start", "end"))
    context = iter(context)

    _xevt, xmeta = next(context)

    # todo: refactor this into a custom func within the module
    me = parse_xml_recursive(context, has_xmlns=False, _mapping=_mapping)

    if isinstance(me, str) or me is None:
        return None

    process_general_attributes(me, flavor='hmdb')

    return HMDBData(**me)
