import sys

from eme.data_access import get_repo

from core.dal.entities.dbdata.ChEBIData import ChEBIData
from core.dal.repositories.ChebiDataRepository import ChebiDataRepository
from modules.db_builder.services.fileparsing import parse_iter_sdf


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

        for r in parse_iter_sdf(self.path, _mapping=self.mapping):
            # if i < 359:
            #     i+=1
            #     continue

            r['chebi_id'] = r['chebi_id'].lstrip('CHEBI:')

            strip_attr(r, 'hmdb_id', 'HMDB')
            strip_attr(r, 'inchi', 'InChI=')
            force_list(r, 'chebi_id_alt')

            # filter out pubchem substrate IDs
            # todo: refactor to a func
            if 'pubchem_id' in r:
                p = r['pubchem_id']
                if isinstance(p, list):
                    p = list(map(lambda p: p[5:], filter(lambda p: p.startswith('CID:'), p)))

                    if len(p) > 1:
                        pass
                    elif len(p) == 0:
                        del r['pubchem_id']
                    else:
                        # after filtering pubchem_id becomes scalar:
                        p = p[0]

                r['pubchem_id'] = p

            # todo: do something with None (=mol struct) key
            r.pop(None)

            data = ChEBIData(**r)
            repo.create(data, commit=False)

            i += 1
            if i % 1000 == 0:
                print(f"\r{i} parsed...", end='')

            if i % 10000 == 0:
                repo.save()
                print("Committed to DB")

        repo.save()
        print("Committed to DB")
