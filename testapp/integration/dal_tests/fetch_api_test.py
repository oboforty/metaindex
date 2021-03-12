from core.dal import MetaboliteView
from core.discovery import getdb
from testapp.utils.testutils import gecc


_api = [
    # todo: HMDB is buggy
    ##('hmdb_id', '0000010'),
    #('pubchem_id', '440624'),
    #('kegg_id', 'C05299'),
    #('kegg_id', 'C02838')

    # todo: ITT:
    ('chebi_id', '1189'),
    #('lipidmaps_id', 'ST02010033'),
    #('metlin_id', '2578')
]

for db_tag, db_id in _api:
    hand = getdb(db_tag)

    print(f"\rFetching {db_tag} = {db_id}...", end="")
    api_resp = hand.fetch_api(db_id, meta_view=False)

    print(f"\r{db_id} ({db_tag}) ==> {api_resp}")
