from flask import render_template


class HomeController():
    def __init__(self, server):
        pass

    def welcome(self):
        return render_template('/home/index.html', page='index')

    def get_about(self):
        return render_template('/home/about.html')

    def get_sources(self):
        return render_template('/home/sources.html')

    def get_citing(self):
        return render_template('/home/citing.html')

    def get_tools(self):
        return render_template('/home/tools.html')

    def get_terms(self):
        return render_template('/home/terms.html')
