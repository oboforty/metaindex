from flask import render_template


class HomeController():
    def __init__(self, server):

        server.preset_endpoints({
            'GET /search-molecules': 'Home:get_molsearch'
        })

    def get_search(self):
        return render_template('/search/index.html')

    def get_molsearch(self):
        return render_template('/search/molsearch.html')

    def get_discovery(self):
        return render_template('/search/discovery.html')


    def get_terms(self):
        return render_template('/home/terms.html')

    def get_api(self):
        return render_template('/home/api.html')
