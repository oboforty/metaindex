from eme.data_access import get_repo

from core.dal import LipidMapsData, LipidMapsDataRepository

from modules.db_builder.services import ding, cardinality
from modules.db_builder.parsers.lipidmaps.parsers import metajson_transform, _mapping
from modules.db_builder.parsers.fileparsing import parse_iter_sdf


class LipidMapsExplorer:

    def __init__(self, conf):
        self.path = conf['base'] + conf['lipidmaps_sdf']
        self.incl_one = conf.get('include_card_one', True)

    def import_db(self, autoclear:bool=False):
        repo: LipidMapsDataRepository = get_repo(LipidMapsData)

        if repo.count() > 0:
            print("LipidMaps Data is not empty. Truncate the table? Y/n:", end="")
            if autoclear or input().lower() == 'y':
                print("Clearing DB")
                repo.delete_all()
            else:
                print("Exited")
                return
        i = 0

        for me in parse_iter_sdf(self.path, _mapping=_mapping):
            # todo: do something with None (=mol struct) key
            me.pop(None, None)

            metajson_transform(me)

            data = LipidMapsData(**me)
            repo.create(data, commit=False)

            if i % 2000 == 0:
                print(f"\rInserting... {i}", end="")
            i+=1
            if i % 10000 == 0:
                repo.save()
                print(" Committed")

        repo.save()
        print(" Committed everything to DB")
        ding.ding()
        ding.ding()
        ding.ding()

    def run(self):
        v_card_max, v_card_count = cardinality.start_count()

        i = 0

        for me in parse_iter_sdf(self.path, _mapping=_mapping):
            metajson_transform(me)

            cardinality.count_cardinality(me, v_card_max, v_card_count)

            if i % 5000 == 0:
                print(f"\rParsing... {i}", end="")
            i+=1

            # if i > 1000:
            #    break

        cardinality.print_cardinality_statistics(v_card_max, v_card_count, mcard=["names"], include_one=self.incl_one)

        print("Total: ", i)
        ding.ding()
