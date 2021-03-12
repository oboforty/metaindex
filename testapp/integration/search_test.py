from core.dal import MetaboliteScalar
from core.metabolite import search_metabolite
from modules.search import clear_table

# clear search table
from modules.search.services.search import init_search

CACHE = True

if CACHE:
    clear_table()

init_search(None, dict(
    MetaboliteView={
        "attributes": [
            'chebi_id', 'kegg_id', 'hmdb_id', 'lipidmaps_id', 'pubchem_id',
            'names', 'mass', 'smiles', 'inchi', 'formula'
        ]
    }
))

res = search_metabolite('18102', 'chebi_id', verbose=True, cache=CACHE)

print(res)
