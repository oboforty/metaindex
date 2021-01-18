from core.managers.ChebiManager import ChebiManager
from core.managers.HmdbManager import HmdbManager
from core.managers.LipidMapsManager import LipidMapsManager

from core.dal.entities.Metabolite import Metabolite
from core.managers.ManagerBase import ManagerBase
from core.settings import getcfg
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
