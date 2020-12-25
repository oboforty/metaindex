import os
import sys

from eme.entities import load_handlers, load_settings
from eme.website import WebsiteBlueprint

from .services import auth

module_path = os.path.dirname(os.path.realpath(__file__))
conf = load_settings(os.path.join(module_path, 'config.ini'))
sys.path.append(module_path)


blueprint = None


def init_webapp(webapp, webconf):
    # TODO: ITT: test with eme first?

    auth.init(webapp, conf['auth'])

    global blueprint

    blueprint = WebsiteBlueprint('doors', conf, module_path, module_route="/users")


def init_cliapp(app, conf):
    app.commands.update(load_handlers(app, 'Command', path=os.path.join(module_path, 'commands')))


def init_wsapp(app, conf):
    pass


def init_dal():
    pass


def init_migration():
    from .dal.user import User
