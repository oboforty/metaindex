from collections import defaultdict

from core.dal.entities.dbdata.kegg import KeggData

from modules.db_builder.parsers.lib import strip_attr, force_list, flatten_refs, force_flatten_extra_refs

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

    force_flatten_extra_refs(me)


def parse_kegg(db_id, content):
    """
    https://www.kegg.jp/kegg/docs/dbentry.html

    :param db_id:
    :param content:
    :return:
    """

    content = content.split('\n')
    data = defaultdict(list)
    _refs = defaultdict(list)
    handle = iter(content)
    kegg_id = db_id

    # smart guess whitespace from 1st line
    line = next(handle)
    try:
        FL = line.index(db_id.upper())
    except:
        return None

    state = None
    for line in handle:
        if line.startswith('///') or line == '':
            # /// skips idk
            continue

        if not line.startswith("   "):
            # interpret labels as regular lines, but save the label
            state = line.split()[0]
            line = line[FL:].rstrip('\n')
        else:
            line = line.lstrip().rstrip('\n')

        if 'ENTRY' == state:
            kegg_id = line
        elif 'DBLINKS' == state:
            # foreign references:
            db_tag, ref_ids = line.split(': ')

            if db_tag.endswith('_id'):
                db_tag = db_tag[:-3]
            db_tag = db_tag.lower()

            for db_id in ref_ids.split(" "):
                _refs[db_tag].append(db_id)
        else:
            data[state].append(line)
            # todo: parse rest of file
            pass

    # merge and transform to standard json
    data.update(_refs)
    metajson_transform(data)

    return KeggData(kegg_id=kegg_id, **data)
