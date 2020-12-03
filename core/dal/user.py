from core.dal.base.sqlite import EntityBase
from core.dal.base.usermixin import UserMixin
from eme.data_access import GUID
from sqlalchemy.orm import relationship
from sqlalchemy import Column, SmallInteger, String, ForeignKey



class User(UserMixin, EntityBase):
    __tablename__ = 'users'

    # World
    wid = Column(GUID(), ForeignKey('worlds.wid', ondelete='CASCADE'))
    world = relationship("World", foreign_keys=[wid])
    iso = Column(String(5))

    # Geopoly player account:
    xp = Column(SmallInteger)
    elo = Column(SmallInteger)
    lauren = Column(SmallInteger)
    sapphire = Column(SmallInteger)
    emerald = Column(SmallInteger)

    def __init__(self, **kwargs):
        self.uid = kwargs.get("uid")
        self.username = kwargs.get("username")

        self.face = kwargs.get("face")
        self.points = kwargs.get("points")
        self.admin = kwargs.get("admin")

        if not isinstance(self.admin, bool):
            self.admin = bool(self.admin)

        self.wid = kwargs.get("wid")
        self.iso = kwargs.get("iso")

        self.xp = kwargs.get("xp", 0)
        self.elo = kwargs.get("elo", 0)
        self.lauren = kwargs.get("lauren", 0)
        self.sapphire = kwargs.get("sapphire", 0)
        self.emerald = kwargs.get("emerald", 0)

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
    def full_info(self):
        return {
            'uid': self.uid,
            'username': self.username,
            'face': self.face,
            'admin': self.admin,
            'wid': self.wid,
            'iso': self.iso,
            'xp': self.xp,
            'elo': self.elo,
            'lauren': self.lauren,
            'sapphire': self.sapphire,
            'emerald': self.emerald,
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
