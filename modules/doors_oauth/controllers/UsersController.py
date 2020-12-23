from flask import url_for, render_template, request
from flask_login import current_user, logout_user
from werkzeug.utils import redirect

from eme.data_access import get_repo

from modules.doors_oauth.dal.repository import UserRepository
from modules.doors_oauth.dal.user import User
from modules.doors_oauth.services import auth


class UsersController():
    def __init__(self, server):
        self.server = server
        self.repo: UserRepository = get_repo(User)

    def get_list(self):
        if not current_user.admin:
            return redirect(url_for('Home.welcome'))

        return ""

    @auth.login_forbidden
    def auth(self):
        if current_user.is_authenticated:
            return "already logged in"

        if 'code' in request.args:
            # 2nd step in authorization: authorization code provided
            code = request.args['code']
            state = request.args['state']

            # get access token
            access_token = auth.fetch_token(code)

            # todo --------------------------------
            # todo: itt: user is None!
            # todo --------------------------------

            # store user in DB
            user = auth.fetch_user(access_token)
            user.access_token = access_token

            self.repo.create(user)

            # we do not rely on access_token, but sessions for the web interface!
            auth.login_user(user, remember=True)

            return redirect('/')

        return redirect(auth.get_authorize_url())

    def get_logout(self):
        logout_user()

        return redirect('/')