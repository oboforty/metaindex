from .managers.ChebiManager import ChebiManager
from .managers.HmdbManager import HmdbManager
from .managers.LipidMapsManager import LipidMapsManager
from .managers.KeggManager import KeggManager
from .managers.PubchemManager import PubchemManager
from .managers.ManagerBase import ManagerBase

from core.dal import Metabolite
from .settings import getcfg
from typing import Dict

dbs = getcfg('discovery.databases')


db_managers: Dict[str, ManagerBase] = {
    'chebi': ChebiManager(getcfg('hmdb')),
    'hmdb': HmdbManager(getcfg('chebi')),
    'lipidmaps': LipidMapsManager(getcfg('lipidmaps')),
    'kegg': KeggManager(getcfg('kegg')),
    'pubchem': PubchemManager(getcfg('pubchem')),
}


def getdb(dbid):
    dbid = dbid.lower()
    if '_id' in dbid:
        dbid = dbid[:-3]

    return db_managers.get(dbid, None)


def get_db_ids():
    return map(lambda s: s+'_id', db_managers.keys())


def query_metabolite(metabolite: Metabolite):

    for db in dbs:
        _ids = getattr(metabolite, db+'_id')
        _data = getdb(db).query_multiple(_ids)

        # todo: itt: what to do with this? how to present?

    # todo: return a View?
