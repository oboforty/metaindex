from core.dal.base.sqlite import EntityBase
from eme.data_access import GUID
from sqlalchemy.orm import relationship
from sqlalchemy import Column, SmallInteger, String, ForeignKey

from ..dal.user_mixin import UserMixin


class User(UserMixin, EntityBase):
    __tablename__ = 'users'

    def __init__(self, **kwargs):
        self.uid = kwargs.get("uid")
        self.username = kwargs.get("username")

        self.face = kwargs.get("face")
        self.points = kwargs.get("points")
        self.admin = kwargs.get("admin")

        if not isinstance(self.admin, bool):
            self.admin = bool(self.admin)

    @property
    def view(self):
        return {
            'uid': self.uid,
            'username': self.username,
            'face': self.face,
            'points': self.points,
            'admin': self.admin,
        }

    @property
    def token_view(self):
        # used for mock auth server
        return {
            "token_type": "Bearer",
            "scope": "profile",

            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_in": self.expires_in,
            "expires_at": self.expires_at,
            "issued_at": self.issued_at
        }
