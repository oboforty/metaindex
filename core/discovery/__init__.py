# DB handlers:
from core.discovery.db_handler import getdb, db_managers

# discovery algorithm & useful util funcs:
from core.discovery.disco import resolve_metabolites, resolve_single_id
from core.discovery.utils import id_to_url, guess_db, pad_id, depad_id


def get_settings():

    return {
        "databases": list(db_managers.keys())
    }
