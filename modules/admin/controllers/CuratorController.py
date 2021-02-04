from flask import url_for, render_template, request
from flask_login import current_user, logout_user
from werkzeug.utils import redirect


class CuratorController():
    def __init__(self, server):
        self.server = server
        self.group = 'Curator'
        self.route = 'curator'

    def get(self):
        if not current_user.curator:
            return redirect(url_for('Home:welcome'))

        return render_template('dashboard/curators.html')
