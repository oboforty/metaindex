from collections import defaultdict


def parse_xml_recursive(context, cur_elem=None, _mapping: dict = None, tag_path=None, has_xmlns=True):
    items = defaultdict(list)

    if _mapping is None:
        _mapping = {}

    if cur_elem and cur_elem.attrib:
        items.update(cur_elem.attrib)

    text = None
    if tag_path is None:
        tag_path = []

    for action, elem in context:
        # print("{0:>6} : {1:20} {2:20} '{3}'".format(action, elem.tag, elem.attrib, str(elem.text).strip()))

        if action == "start":
            tag = elem.tag.split('}', 1)[1] if has_xmlns else elem.tag
            tag_path.append(tag)
            state = '.'.join(tag_path)
            state = _mapping.get(state.lower(), tag)

            items[state].append(parse_xml_recursive(context, elem, _mapping=_mapping, tag_path=tag_path, has_xmlns=has_xmlns))
        elif action == "end":
            text = elem.text.strip() if elem.text else None

            #tag = elem.tag.split('}', 1)[1]
            if tag_path:
                tag_path.pop()

            elem.clear()
            break

    if len(items) == 0:
        return text

    return items
    #{ k: v[0] if len(v) == 1 else v for k, v in items.items() }


def parse_iter_sdf(fn, _mapping: dict = None):
    if _mapping is None:
        _mapping = {}

    with open(fn, 'r', encoding='utf8') as fh:
        buffer = {}
        state = None

        for line in fh:
            line = line.rstrip('\n')

            if line.startswith('$$$$'):
                # New entry
                yield buffer
                state = None
                buffer = {}
                continue
            elif not line:
                continue
            elif line.startswith('>'):
                state = line[3:-1]
            else:
                if state is None:
                    attr = None
                else:
                    attr = _mapping.get(state.lower(), state)

                if attr in buffer:
                    # there are multiple entries in buffer, create a list
                    val = buffer[attr]

                    if isinstance(val, list):
                        buffer[attr].append(line)
                    else:
                        buffer[attr] = [val, line]
                else:
                    buffer[attr] = line
