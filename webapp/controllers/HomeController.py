from flask import render_template


class HomeController():
    def __init__(self, server):

        server.preset_endpoints({
            'GET /search-molecules': 'Home:get_molsearch'
        })

    def welcome(self):
        return render_template('/search/index.html', page='index')

    def get_molsearch(self):
        return render_template('/search/molsearch.html', page='index')

    def get_terms(self):
        return render_template('/home/terms.html')
