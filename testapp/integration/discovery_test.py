from core.dal import MetaboliteView
from core.discovery import resolve_single_id, resolve_metabolites


mv: MetaboliteView
mv, stats = resolve_single_id('chebi_id', '1189', verbose=True)


for _oof, _v in stats.items():
    print(_oof, _v)

print("\nReferences:\n")

for db_tag, db_id in mv.refs:
    print(db_tag, '=', db_id)
