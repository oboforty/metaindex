import os
import sys

from eme.entities import load_handlers, load_settings
from eme.website import WebsiteBlueprint
from eme.data_access import get_repo

from core.dal import User
from .groups.UsersGroup import UsersGroup
from .services import auth

module_path = os.path.dirname(os.path.realpath(__file__))
conf = load_settings(os.path.join(module_path, 'config.ini'))
sys.path.append(module_path)


blueprint = None


def init_webapp(webapp, webconf):
    # TODO: ITT: test with eme first?
    from core.dal import User

    auth.init(webapp, conf['auth'], get_repo(User))

    global blueprint

    blueprint = WebsiteBlueprint('doors', conf, module_path, module_route="/users")


def init_cliapp(app, conf):
    app.commands.update(load_handlers(app, 'Command', path=os.path.join(module_path, 'commands')))


def init_wsapp(app, wsconf):
    auth.init_ws(app, conf, get_repo(User))

    app.load_groups({"Users": UsersGroup(app)}, conf=conf)


def init_dal():
    pass


def init_migration():
    pass
