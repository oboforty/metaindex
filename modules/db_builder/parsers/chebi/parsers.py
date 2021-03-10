from modules.db_builder.parsers.lib import strip_attr, force_list, flatten_refs, force_flatten_extra_refs
from modules.db_builder.parsers.pubchem.utils import split_pubchem_ids

_mapping: dict


def init_mapping(_map):
    global _mapping
    _mapping = _map


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
