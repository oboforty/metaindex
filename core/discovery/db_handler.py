from .managers.ChebiManager import ChebiManager
from .managers.HmdbManager import HmdbManager
from .managers.LipidMapsManager import LipidMapsManager
from .managers.ManagerBase import ManagerBase

from core.dal import Metabolite
from .settings import getcfg
from typing import Dict

dbs = getcfg('discovery.databases')


db_managers: Dict[str, ManagerBase] = {
    'chebi': ChebiManager(),
    'hmdb': HmdbManager(),
    'lipidmaps': LipidMapsManager(),
}


def getdb(dbid):
    dbid = dbid.lower()
    if '_id' in dbid:
        dbid = dbid[:-3]

    return db_managers[dbid]


def query_metabolite(metabolite: Metabolite):

    for db in dbs:
        _ids = getattr(metabolite, db+'_id')
        _data = getdb(db).query_multiple(_ids)

        # todo: itt: what to do with this? how to present?

    # todo: return a View?
