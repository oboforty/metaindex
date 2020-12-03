import uuid

from eme.data_access import GUID, JSON_GEN
from sqlalchemy import Column, ForeignKey, SmallInteger, String, Boolean
from sqlalchemy.orm import relationship

from core.dal.base.sqlite import EntityBase


class Area(EntityBase):
    __tablename__ = 'areas'

    aid = Column(GUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String(20))

    owner_iso = Column(String(5))
    # if area belonging to town
    town_iso = Column(String(5), default=None)

    active_spell = Column(GUID())

    soldiers = relationship("soldiers", foreign_keys="soldiers.sid")
