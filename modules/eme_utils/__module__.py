import os
import sys

from eme.entities import load_handlers, load_settings

from .services.error_reporting import init_ws
from .services.jinja_helpers import init_jinja
from .services.mail import init_mail


module_path = os.path.dirname(os.path.realpath(__file__))
conf = load_settings(os.path.join(module_path, 'config.ini'))
sys.path.append(module_path)

def init_webapp(app, webconf):
    init_jinja(app, webconf)

    init_mail(app, conf['mail'])


def init_cliapp(app, conf):
    app.commands.update(load_handlers(app, 'Command', path=os.path.join(module_path, 'commands')))


def init_wsapp(app, conf):
    init_ws(app, conf)


def init_dal():
    pass


def init_migration():
    pass
