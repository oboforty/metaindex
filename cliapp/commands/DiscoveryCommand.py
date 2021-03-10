from core.dal import MetaboliteView
from core.discovery import resolve_single_id, resolve_metabolites


class DiscoveryCommand:

    def __init__(self, cli):
        self.cli = cli
        self.conf = cli.conf

    def run(self, db_tag, db_id, store_cache: bool = False):
        mv: MetaboliteView
        mv, stats = resolve_single_id(db_tag, db_id, verbose=True, cache=store_cache)

        if store_cache:
            # store in database
            pass


            # create search term
            pass


        # Print stats
        for _oof, _v in stats.items():
            print(_oof, _v)

        print("\nReferences:\n")

        for db_tag, db_id in mv.refs:
            print(db_tag, '=', db_id)
