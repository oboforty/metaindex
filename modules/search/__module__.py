import os
import sys

from eme.entities import load_handlers, load_settings

from .services.search import init_search


module_path = os.path.dirname(os.path.realpath(__file__))
conf = load_settings(os.path.join(module_path, 'config.ini'))
sys.path.append(module_path)

def init_webapp(app, webconf):
    init_search(app, conf)


def init_cliapp(app, conf):
    app.commands.update(load_handlers(app, 'Command', path=os.path.join(module_path, 'commands')))


def init_wsapp(app, conf):
    pass


def init_dal():
    pass


def init_migration():
    from .dal.entities.SearchItem import SearchItem
