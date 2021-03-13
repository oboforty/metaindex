

def flatten_chebi_api_attr(ch: dict, attr, _mapping: dict):
    val = ch.pop(attr)

    if isinstance(val, list):
        if isinstance(val[0], dict):
            if 'data' in val[0]:
                # list of dicts
                val = [el['data'] for el in val]
            else:
                # todo: odd composite value, should we parse these?
                # e.g. OntologyParents -> {chebiName, chebiId}
                pass
        else:
            # list of str
            pass # noop

    elif isinstance(val, dict):
        if 'data' in val:
            val = [val['data']]
        else:
            # todo: odd composite value, should we parse these?
            # e.g. ChemicalStructures -> {structure, type, dimension, defaultStructure}
            pass

    # make list of similar attributes
    newattr = _mapping.get(attr.lower(), attr.lower())
    if newattr not in ch:
        ch[newattr] = []
    ch[newattr].append(val)
