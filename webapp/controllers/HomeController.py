from flask import render_template


class HomeController():
    def __init__(self, server):
        pass

    def welcome(self):
        return render_template('/home/index.html', page='index')

    def get_terms(self):
        return render_template('/home/terms.html')
