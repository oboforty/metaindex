from eme.data_access import get_repo

from core.dal.entities.dbdata.ChEBIData import ChEBIData
from core.dal.repositories.ChebiDataRepository import ChebiDataRepository
from modules.db_builder.services.fileparsing import parse_iter_sdf


class ChebiInserter:

    def __init__(self, conf):
        self.path = conf['bulk_db']['base'] + conf['bulk_db']['chebi_sdf']
        self.mapping = conf['mapping_chebi']
        self.mcard = self.mapping.pop('__card__')

    def run(self):
        repo: ChebiDataRepository = get_repo(ChEBIData)

        if repo.count() > 0:
            print("Chebi Data is not empty. Truncate the table? Y/n:", end="")
            if input().lower() == 'y':
                print("Clearing DB")
                repo.delete_all()
            else:
                print("Exited")
                return

        for r in parse_iter_sdf(self.path):
            r['inchi'] = r['inchi'].lstrip('InChI=')
            r['chebi_id'] = r['chebi_id'].lstrip('CHEBI:')

            # filter out pubchem substrate IDs
            p = r['pubchem_id']
            if p is list:
                p = list(map(lambda p: p[4:],filter(lambda p: p.startswith('CID:'), p)))

                if len(p) > 1:
                    pass
                elif len(p) == 0:
                    del r['pubchem_id']
                else:
                    r['pubchem_id'] = p[0]

            data = ChEBIData(**r)
            repo.create(data, commit=False)

        repo.commit()
