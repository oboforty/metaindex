import os
import sys

from eme.entities import load_handlers, load_settings

module_path = os.path.dirname(os.path.realpath(__file__))
conf = load_settings(os.path.join(module_path, 'config.ini'))
sys.path.append(module_path)
"""
This module is responsible for exploring and inserting the various meta db dumps into our db
"""


def init_webapp(app, webconf):
    pass


def init_cliapp(app, cliconf):
    app.commands.update(load_handlers(app, 'Command', path=os.path.join(module_path, 'commands')))

    xpl = app.commands['Explore']
    ins = app.commands['Insert']
    xpl.explorers = load_handlers(conf['bulk_db'], 'Explorer', path=os.path.join(module_path, 'explorers'))
    ins.inserters = xpl.explorers


def init_wsapp(app, conf):
    pass


def init_dal():
    pass


def init_migration():
    # todo: @Later: check if DBs are filled, but only give warning to dev
    pass
