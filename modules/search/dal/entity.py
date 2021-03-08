from sqlalchemy import Column, String

from core.dal import EntityBase

"""
Add levensthein distance (EME?)
 https://towardsdatascience.com/fuzzy-matching-with-levenshtein-and-postgresql-ed66cad01c03

"""
class SearchItem(EntityBase):
    __tablename__ = 'search_items'

    # TODO: order of pkey
    search_attr = Column(String(64), nullable=False)
    search_value = Column(String(128), nullable=False)

    entity_type = Column(String(64))
    entity_id = Column(String(64))

    # flask endpoint or url
    url = Column(String(256))
