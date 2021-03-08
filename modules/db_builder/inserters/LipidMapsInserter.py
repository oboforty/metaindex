from eme.data_access import get_repo

from core.dal import LipidMapsData, LipidMapsDataRepository

from modules.db_builder.services.ding import ding
from modules.db_builder.services.fileparsing import parse_iter_sdf
from modules.db_builder.services.attr_parsing import process_general_attributes


class LipidMapsInserter:

    def __init__(self, conf):
        self.path = conf['bulk_db']['base'] + conf['bulk_db']['lipidmaps_sdf']
        self.mapping = conf['mapping_lipidmaps']
        self.mcard = self.mapping.get('__card__')

    def run(self, autoclear:bool=False):
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

        for me in parse_iter_sdf(self.path, _mapping=self.mapping):
            process_general_attributes(me, flavor='lipidmaps')

            # todo: do something with None (=mol struct) key
            me.pop(None, None)

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
        ding()
        ding()
        ding()
