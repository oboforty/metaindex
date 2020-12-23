import uuid

from sqlalchemy import Column, Integer, String, Boolean, SmallInteger, ForeignKey, ForeignKeyConstraint, Date, DateTime, \
    TIMESTAMP, func, Float

from eme.data_access import GUID, JSON_GEN
from eme.data_access import Repository

from core.dal.base.sqlite import EntityBase

"""
Add levensthein distance (EME?)
 https://towardsdatascience.com/fuzzy-matching-with-levenshtein-and-postgresql-ed66cad01c03

"""
class SearchItem(EntityBase):
    __tablename__ = 'search_items'

    search_value = Column(String(128), primary_key=True, nullable=False)
    search_key = Column(String(64), primary_key=True, nullable=False)

    result_value = Column(String(128), nullable=False)
    result_key = Column(String(64), nullable=True)

