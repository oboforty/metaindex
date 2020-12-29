from modules.db_builder.services.fileparsing import parse_iter_sdf
from modules.db_builder.services.attr_parsing import process_general_attributes
from modules.db_builder.services.cardinality import count_cardinality, start_count, print_cardinality_statistics


class LipidMapsExplorer:

    def __init__(self, conf):
        self.path = conf['bulk_db']['base'] + conf['bulk_db']['lipidmaps_sdf']
        self.mapping = conf['mapping_lipidmaps']
        self.mcard = self.mapping.get('__card__')
        self.incl_one = conf.get('explore.include_card_one', True)

    def run(self):
        v_card_max, v_card_count = start_count()

        i = 0

        for me in parse_iter_sdf(self.path, _mapping=self.mapping):
            process_general_attributes(me, flavor='lipidmaps')

            count_cardinality(me, v_card_max, v_card_count)

            if i % 5000 == 0:
                print(f"\rParsing... {i}", end="")
            i+=1

            #if i > 1000:
            #    break

        print_cardinality_statistics(v_card_max, v_card_count, mcard=self.mcard, include_one=self.incl_one)

        print("Total: ", i)
