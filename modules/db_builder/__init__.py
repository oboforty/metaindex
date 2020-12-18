import os
from eme.entities import load_handlers, load_settings


conf = load_settings(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini'))

"""
This module is responsible for exploring and inserting the various meta db dumps into our db
"""

def init_webapp(app, webconf):
    pass

def init_cliapp(app, cliconf):
    app.commands.update(load_handlers(app, 'Command', 'modules/db_builder/handlers/commands'))

    xpl = app.commands['Explore']
    xpl.explorers = load_handlers(conf, 'Explorer', 'modules/db_builder/handlers/explorers')

    spuderman = app.commands['Scan']
    spuderman.scanners = load_handlers(conf, 'Scanner', 'modules/db_builder/handlers/scanners')

    insert = app.commands['Insert']
    insert.inserters = load_handlers(conf, 'Inserter', 'modules/db_builder/handlers/inserters')


def init_wsapp(app, conf):
    pass

def init_dal():
    pass
