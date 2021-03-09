from core.dal import MetaboliteView
from core.discovery import getdb
from testapp.utils.testutils import gecc


_test_primary = [
    ('hmdb_id', 'HMDB0000010'),
    ('hmdb_id', 'HMDB0029703'),
    ('hmdb_id', '0060039'),

    ('chebi_id', '10'),
    ('chebi_id', '100'),
    ('chebi_id', '10000'),
    ('chebi_id', '100657'),
    ('chebi_id', '32350'),
    ('chebi_id', 'CHEBI:86419'),
    ('chebi_id', 'CHEBI:137768'),

    ('lipidmaps_id', 'LMFA01030244'),
    ('lipidmaps_id', 'FA01030327'),
]


"""
  Primary database queries
"""
print("\nPrimary queries:")
for db_tag, db_id in _test_primary:
    hand = getdb(db_tag)

    print(f"\rQuerying {db_tag} = {db_id}...", end="")

    res: MetaboliteView = hand.query_primary(db_id)
    print(f"\r{db_id} ({db_tag}) ==> {res}")
