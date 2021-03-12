from sqlalchemy import Column, String

from core.dal import EntityBase


class SearchItem(EntityBase):
    __tablename__ = 'search_items'

    search_term = Column(String(128), nullable=False, primary_key=True)
    search_attr = Column(String(128), nullable=False, primary_key=True)

    entity_id = Column(String(64))
    endpoint = Column(String(64))

    def __init__(self, **kwargs):
        self.search_attr = kwargs.get('search_attr')
        self.search_term = kwargs.get('search_term')
        self.entity_id = kwargs.get('entity_id')
        self.endpoint = kwargs.get('endpoint')
