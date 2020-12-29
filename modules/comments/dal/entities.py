import uuid
from time import time

from eme.data_access import GUID
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from core.dal.base.sqlite import EntityBase
from modules.doors_oauth.dal.user import User


class Comment(EntityBase):
    __tablename__ = 'comments'

    cid = Column(GUID(), primary_key=True, default=uuid.uuid4)
    content = Column(Text)
    created_at = Column(Integer, nullable=False, default=lambda: int(time()))

    author_id = Column(GUID(), ForeignKey('users.uid', ondelete='CASCADE'))
    author = relationship("User", foreign_keys=[author_id], lazy='joined') # eager loading

    parent_id = Column(GUID(), ForeignKey('comments.cid', ondelete='CASCADE'))
    reply_to = relationship("Comment", foreign_keys=[parent_id], lazy='select') # lazy loading

    entity_id = Column(String(128))
    entity_type = Column(String(32))

    @property
    def view(self):
        return {
            "cid": self.cid,
            "content": self.content,
            "author": self.author.view,
            "created_at": self.created_at,
            "parent_id": self.parent_id,
            "entity_id": self.entity_id,
            "entity_type": self.entity_type,
        }

    @property
    def view_strict(self):
        return {
            "cid": self.cid,
            "content": self.content,
            "author_id": self.author_id,
            "created_at": self.created_at,
            "parent_id": self.parent_id,
            "entity_id": self.entity_id,
            "entity_type": self.entity_type,
        }
