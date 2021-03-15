from core.dal import MetaboliteScalar
from core.metabolite import search_metabolite
from modules.search import clear_table

CACHE = True

if CACHE:
    clear_table()


res = search_metabolite('17883', 'chebi_id', verbose=True, cache=CACHE)

print(res)
