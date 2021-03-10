from collections import defaultdict

from ..parsers.lib import rlen


def start_count():
    a,b = defaultdict(int), defaultdict(int)

    _keys = [
        "chebi_id",
        "hmdb_id",
        "lipidmaps_id",
        "kegg_id",
        "pubchem_id",
        "chebi_id_alt",
        "hmdb_id_alt",
        "lipidmaps_id_alt",
        "kegg_id_alt",
        "pubchem_id_alt",
        "cas_id",
        "inchi", "inchikey", "smiles",
        "names", "formula",
    ]

    for _key in _keys:
        a.setdefault(_key, 0)
        b.setdefault(_key, 0)

    return a,b


def count_cardinality(v: dict, card_max: dict, card_occurences: dict):
    for key,val in v.items():
        if key is None:
            continue

        card = rlen(val)

        # max search:
        if card_max[key] < card: card_max[key] = card
        # count occurences over card of 1:
        if card > 1:
            card_occurences[key] += 1


def print_cardinality_statistics(v_card_max, v_card_count, mcard, include_one=True):
    print("Conf multiple card:", mcard)
    print("Actual multiple card:", list(filter(lambda c: v_card_max[c] > 1, v_card_max.keys())))

    print("Detected cardinalities:")
    print("{0:<40} {1:<10}  {2:<10}".format('attr', 'cardinality', '# of card>1'))
    for key, val in v_card_max.items():
        if not include_one and val<=1:
            continue

        print(f"{key:<44} {val:<10} {v_card_count[key]:<10}")

    print("-------------------------------------")
    print("")

