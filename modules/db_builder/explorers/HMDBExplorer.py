from modules.db_builder.services.ding import ding
from modules.db_builder.services.fileparsing import parse_xml_recursive
from modules.db_builder.services.attr_parsing import process_general_attributes
from modules.db_builder.services.cardinality import count_cardinality, start_count, print_cardinality_statistics

import xml.etree.ElementTree as ET


class HMDBExplorer:

    def __init__(self, conf):
        self.path = conf['bulk_db']['base'] + conf['bulk_db']['hmdb_xml']
        self.mapping = conf['mapping_hmdb']
        self.mcard = self.mapping.get('__card__')
        self.incl_one = conf.get('explore.include_card_one', True)

    def run(self):
        # parse XML file:
        context = ET.iterparse(self.path, events=("start", "end"))
        context = iter(context)

        ev_1, xroot = next(context)
        i = 0

        v_card_max, v_card_count = start_count()

        for ev_2, xmeta in context:
            # Úgy még sosem volt, hogy valahogy ne lett volna
            me = parse_xml_recursive(context, _mapping=self.mapping)

            if isinstance(me, str) or me is None:
                continue

            process_general_attributes(me, flavor='hmdb')

            count_cardinality(me, v_card_max, v_card_count)

            if i % 500 == 0:
                print(f"\rParsing... {i}", end="")
            i += 1

            # if i > 200:
            #     break

        print_cardinality_statistics(v_card_max, v_card_count, mcard=self.mcard, include_one=self.incl_one)

        print("Total: ", i)
        ding()
