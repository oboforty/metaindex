from ..fileparsing import parse_iter_sdf, rlen


def parse_chebi_sdf(path_fn):
    i = 0
    v_card = []
    pc = set()

    for me in parse_iter_sdf(path_fn):
        attr = 'PubChem Database Links'

        if attr in me:
            pubchem_id = list(filter(lambda x: x.startswith('CID:'), me[attr]))

            if rlen(pubchem_id) > 1:
                v_card.append([me['ChEBI ID'], pubchem_id])

        # i += 1
        # if i % 5000 == 0:
        #     print(i)

    print("CHEBI SDF")
    print(v_card)
    print(pc)
