from eme.data_access import get_repo

from core.dal import HMDBData, HMDBDataRepository

from modules.db_builder.services import cardinality
from modules.db_builder.services.ding import ding
from modules.db_builder.parsers.hmdb.parsers import metajson_transform, _mapping
from modules.db_builder.parsers.fileparsing import parse_xml_recursive

import xml.etree.ElementTree as ET


class HMDBExplorer:

    def __init__(self, conf):
        self.path = conf['base'] + conf['hmdb_xml']
        self.incl_one = conf.get('include_card_one', True)

    def import_db(self, autoclear:bool=False):
        repo: HMDBDataRepository = get_repo(HMDBData)

        if repo.count() > 0:
            print("HMDB Data is not empty. Truncate the table? Y/n:", end="")
            if autoclear or input().lower() == 'y':
                print("Clearing DB")
                repo.delete_all()
            else:
                print("Exited")
                return

        # parse XML file:
        context = ET.iterparse(self.path, events=("start", "end"))
        context = iter(context)

        ev_1, xroot = next(context)
        i = 0

        for ev_2, xmeta in context:
            # Úgy még sosem volt, hogy valahogy ne lett volna
            me = parse_xml_recursive(context, _mapping=_mapping)

            if isinstance(me, str) or me is None:
                continue
            metajson_transform(me)

            data = HMDBData(**me)
            repo.create(data, commit=False)

            if i % 500 == 0:
                print(f"\rInserting... {i}", end="")
            i+=1
            if i % 3000 == 0:
                repo.save()
                print(" Committed")

        repo.save()
        print(" Committed everything to DB")
        ding()
        ding()
        ding()

    def run(self):
        # parse XML file:
        context = ET.iterparse(self.path, events=("start", "end"))
        context = iter(context)

        ev_1, xroot = next(context)
        i = 0

        v_card_max, v_card_count = cardinality.start_count()

        for ev_2, xmeta in context:
            # Úgy még sosem volt, hogy valahogy ne lett volna
            me = parse_xml_recursive(context, _mapping=_mapping)

            if isinstance(me, str) or me is None:
                continue

            metajson_transform(me)

            cardinality.count_cardinality(me, v_card_max, v_card_count)

            if i % 500 == 0:
                print(f"\rParsing... {i}", end="")
            i += 1

            # if i > 200:
            #     break

        cardinality.print_cardinality_statistics(v_card_max, v_card_count, mcard=["names"], include_one=self.incl_one)

        print("Total: ", i)
        ding()
