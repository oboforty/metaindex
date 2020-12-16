import os
from eme.entities import load_handlers, load_settings

from .services.search import init_search


module_path = os.path.dirname(os.path.realpath(__file__))
conf = load_settings(os.path.join(module_path, 'config.ini'))


def init_webapp(app, webconf):
    init_search(app, conf)

def init_cliapp(app, conf):
    app.commands.update(load_handlers('Command', 'commands', module_path))

def init_wsapp(app, conf):
    pass

def init_dal():
    pass
