import random
import string
import time

from eme.data_access import get_repo

from core.dal import User
from modules.doors_oauth import DoorsCachedToken

enabled = False
devuser = None


def init(app, up=None):
    global enabled, devuser

    if up is not None:
        global enabled
        enabled = True
        devuser = tuple(up)


def _safecheck():
    if get_repo(User).count() > 20:
        raise Exception("It seems like developer mode has been enabled on the production website!!")


def authenticate(username1, password1):
    if not enabled or devuser != (username1, password1):
        return None

    _safecheck()

    user = get_repo(User).find_by_username(username1)

    return user


def get_devuser():
    if not enabled:
        return None

    _safecheck()

    user = get_repo(User).find_by_username(devuser[0])
    return user

def generate_token(user: User):
    _safecheck()

    token = ''.join(random.choice(string.ascii_letters) for i in range(10))
    tk = DoorsCachedToken(token, user=user, expires_in=864000, issued_at=time.time())

    user.update_token(tk)
    get_repo(User).save()


def url_postfix():
    if not enabled:
        return None

    return 'username='+devuser[0]+'&password='+devuser[1]

