import os
import sys

from eme.entities import load_handlers, load_settings
from eme.website import WebsiteBlueprint

from .services import devauth

module_path = os.path.dirname(os.path.realpath(__file__))
conf = load_settings(os.path.join(module_path, 'config.ini'))
sys.path.append(module_path)


blueprint = None


def init_webapp(webapp, webconf):
    global blueprint

    blueprint = WebsiteBlueprint('admin', conf, module_path, module_route="/admin")

    # if webapp.develop:
    #     devauth.init(webapp, conf.get('admin.devuser'))
    #     # add 1 additional Api
    #     webapp.load_controllers({"MockedUserController": MockedUserController(webapp)}, conf={
    #         '__debug_len__': 52
    #     })

def init_cliapp(app, conf):
    app.commands.update(load_handlers(app, 'Command', path=os.path.join(module_path, 'commands')))


def init_wsapp(app, conf):
    pass


def init_dal():
    pass


def init_migration():
    pass
