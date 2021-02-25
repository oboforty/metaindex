import logging
import os
from logging.config import dictConfig


def init(conf, app):
    if not conf['debug'] and not conf['develop']:
        dictConfig({
            'version': 1,
            'formatters': {'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }},
            'handlers': {'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            }},
            'root': {
                'level': 'INFO',
                'handlers': ['wsgi']
            }
        })


def init_ws(conf, app):
    return

    # Logging
    logger = logging.getLogger(conf.get('logprefix', 'eme'))
    logger.setLevel(logging.DEBUG)

    # file log
    fh = logging.FileHandler(conf.get('logfile', os.path.join(fbase, 'logs.txt')))
    lvl = conf.get('loglevel', 'WARNING')
    fh.setLevel(getattr(logging, lvl))

    # console log
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    app.logger = logger
