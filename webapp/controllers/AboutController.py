from flask import render_template


class AboutController():
    def __init__(self, server):
        pass

    def welcome(self):
        return render_template('/home/index.html', page='index')

    def get_about(self):
        return render_template('/pages/pages.html')

    def get_sources(self):
        # databases, pages _data DB cardinalities
        return render_template('/pages/sources.html')

    def get_citing(self):
        # how to cite + how to use FE citing editor
        return render_template('/pages/citing.html')

    def get_tools(self):
        # pages tools (package, api, internal tools (e.g. commands) etc)
        return render_template('/pages/tools.html')

    def get_identifier(self):
        # pages meta_id generation
        return render_template('/pages/identifier.html')
