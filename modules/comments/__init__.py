import os
import sys

from eme.data_access import get_repo
from eme.entities import load_handlers, load_settings, SettingWrapper
from eme.website import WebsiteBlueprint


module_path = os.path.dirname(os.path.realpath(__file__))
conf = load_settings(os.path.join(module_path, 'config.ini'))
sys.path.append(module_path)


_apic = conf.view.copy()
_apic['website'] = _apic.pop('api')
conf_api = SettingWrapper(_apic)


blueprints = []


def init_webapp(webapp, webconf):
    global blueprints

    blueprints.extend([
        WebsiteBlueprint('comments', conf, module_path, module_route="/comments"),
        WebsiteBlueprint('comments_api', conf_api, module_path, module_route="/api/comments"),
    ])


def init_cliapp(app, conf):
    app.commands.update(load_handlers(app, 'Command', path=os.path.join(module_path, 'commands')))


def init_wsapp(app, conf):
    pass


def init_dal():
    pass


def init_migration():
    from .dal.entities import Comment
