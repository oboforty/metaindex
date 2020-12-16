from flask import render_template


class HomeController():
    def __init__(self, server):
        pass

    def welcome(self):
        return render_template('/home/index.html')

    def formats(self):
        return render_template('/home/formats.html')

    def pages(self):
        return render_template('/home/vuepages.html')
