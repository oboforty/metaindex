from core.dal import MetaboliteView
from testapp.utils.testutils import gecc
from core.discovery import getdb

_test_reverse = [
    ('chebi_id', ('kegg_id', 'C09981')),
    ('chebi_id', ('pubchem_id', '54657616')),

    ('lipidmaps_id', ('hmdb_id', '0002396')),
    ('lipidmaps_id', ('hmdb_id', 'HMDB0034849')),

    ('hmdb_id', ('chebi_id', '40356')),
    ('hmdb_id', ('chebi_id', 'CHEBI:803536')),
]

"""
  Reverse-primary database queries
"""

print("\nReverse-queries:")
for db_tag, (from_db_tag, from_db_id) in _test_reverse:
    hand = getdb(db_tag)

    mv = MetaboliteView()
    setattr(mv, from_db_tag, {from_db_id})

    print(f"\rReverse-querying {from_db_id} ({from_db_tag})...", end="")

    db_ids = hand.query_reverse(mv)
    _outp = ', '.join(map(lambda x: str(x[0]), db_ids))
    if not _outp: _outp = 'NONE'

    print(f"\rResolved {from_db_tag} = {from_db_id} ==> {db_tag} = {_outp}")
