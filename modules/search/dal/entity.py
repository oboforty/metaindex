from sqlalchemy import Column, String

from core.dal import EntityBase


class SearchItem(EntityBase):
    __tablename__ = 'search_items'

    search_term = Column(String(128), nullable=False, primary_key=True)
    search_attr = Column(String(128), nullable=False, primary_key=True)

    entity_id = Column(String(64))
    endpoint = Column(String(64))
    display = Column(String(128))

    def __init__(self, **kwargs):
        self.search_attr = kwargs.get('search_attr')
        self.search_term = kwargs.get('search_term')
        self.entity_id = kwargs.get('entity_id')
        self.endpoint = kwargs.get('endpoint')
        self.display = kwargs.get('display')

    @property
    def view(self):
        return dict(
            search_attr=self.search_attr,
            search_term=self.search_term,
            entity_id=self.entity_id,
            endpoint=self.endpoint,
            display=self.display,
        )
