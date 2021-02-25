from eme.data_access import get_repo

from core.dal import ChEBIData, ChebiDataRepository

from ..services.ding import ding
from ..services.fileparsing import parse_iter_sdf
from ..services.attr_parsing import process_general_attributes


class ChebiInserter:

    def __init__(self, conf):
        self.path = conf['bulk_db']['base'] + conf['bulk_db']['chebi_sdf']
        self.mapping = conf['mapping_chebi']
        self.mcard = self.mapping.get('__card__')

    def run(self, autoclear:bool=False):
        repo: ChebiDataRepository = get_repo(ChEBIData)

        if repo.count() > 0:
            print("Chebi Data is not empty. Truncate the table? Y/n:", end="")
            if autoclear or input().lower() == 'y':
                print("Clearing DB")
                repo.delete_all()
            else:
                print("Exited")
                return
        i = 0

        for me in parse_iter_sdf(self.path, _mapping=self.mapping):
            process_general_attributes(me, flavor='chebi')

            # todo: do something with None (=mol struct) key
            me.pop(None)

            data = ChEBIData(**me)
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
