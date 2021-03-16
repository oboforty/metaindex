from core.dal import MetaboliteScalar
from core.metabolite import search_metabolite
from modules.search import clear_table


#clear_table()

res = search_metabolite('17883', 'chebi_id', verbose=True)

print(res)
