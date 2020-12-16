import os
from eme.entities import load_handlers, load_settings

from .services.jinja_helpers import init_jinja
from .services.mail import init_mail


conf = load_settings(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini'))


def init_webapp(app, webconf):
    init_jinja(app, webconf)

    init_mail(app, conf['mail'])

def init_cliapp(self, app, conf):
    self.commands = load_handlers(self, 'Command', 'commands', self.module_path)

def init_wsapp(app, conf):
    pass

def init_dal():
    pass
