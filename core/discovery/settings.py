from eme.entities import load_settings

_cfg = load_settings('core/discovery/dbhandlers.ini')


def get_settings():
    return _cfg


def getcfg(opts, default=None, cast=None):
    return _cfg.get(opts, default, cast)
