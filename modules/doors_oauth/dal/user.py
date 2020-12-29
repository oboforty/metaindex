from core.dal.base.sqlite import EntityBase
from sqlalchemy import Column, Boolean

from ..dal.user_mixin import UserMixin


class User(UserMixin, EntityBase):
    __tablename__ = 'users'

    curator = Column(Boolean(), default=False)

    def __init__(self, **kwargs):
        self.uid = kwargs.get("uid")
        self.username = kwargs.get("username")

        self.face = kwargs.get("face")
        self.points = kwargs.get("points")
        self.admin = kwargs.get("admin")
        self.curator = kwargs.get("curator")

        if not isinstance(self.admin, bool):
            self.admin = bool(self.admin)
        if not isinstance(self.curator, bool):
            self.curator = bool(self.curator)

    @property
    def view(self):
        return {
            'uid': self.uid,
            'username': self.username,
            'face': self.face,
            'points': self.points,
            'admin': self.admin,
            'curator': self.curator,
        }

    @property
    def view_full(self):
        return {
            **self.view,
            "token_type": "Bearer",
            "scope": "profile",

            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_in": self.expires_in,
            "expires_at": self.expires_at,
            "issued_at": self.issued_at
        }
