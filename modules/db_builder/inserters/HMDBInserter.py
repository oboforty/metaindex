from eme.data_access import get_repo

from core.dal import HMDBData, HMDBDataRepository

from modules.db_builder.services.ding import ding
from modules.db_builder.services.fileparsing import parse_xml_recursive
from modules.db_builder.services.attr_parsing import process_general_attributes

import xml.etree.ElementTree as ET


class HMDBInserter:

    def __init__(self, conf):
        self.path = conf['bulk_db']['base'] + conf['bulk_db']['hmdb_xml']
        self.mapping = conf['mapping_hmdb']
        self.mcard = self.mapping.get('__card__')

    def run(self, autoclear:bool=False):
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
            me = parse_xml_recursive(context, _mapping=self.mapping)

            if isinstance(me, str) or me is None:
                continue

            process_general_attributes(me, flavor='hmdb')

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
