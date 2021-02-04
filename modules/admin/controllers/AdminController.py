from flask import url_for, render_template, request
from flask_login import current_user, logout_user
from werkzeug.utils import redirect



class AdminController():
    def __init__(self, server):
        self.server = server
        self.group = 'Admin'
        self.route = 'admin'

    def get(self):
        if not current_user.admin:
            return redirect(url_for('Home:welcome'))

        return render_template('dashboard/admins.html')
