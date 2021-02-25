
from dataclasses import dataclass


@dataclass
class UserView:
    uid: str
    username: str
    admin: bool

    # face: str = None
    client_id: str = None
    client = None

    def __init__(self, **kwargs):
        self.uid = kwargs.get('uid')
        self.username = kwargs.get('username')
        self.admin = kwargs.get('admin')
