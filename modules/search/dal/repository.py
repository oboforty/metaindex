from eme.data_access import Repository, RepositoryBase

from modules.search.dal.entity import SearchItem


@Repository(SearchItem)
class SearchItemRepository(RepositoryBase):

    def search(self, search, attrs=None):
        q = self.session.query(SearchItem) \
            .filter(SearchItem.search_term == search)

        if attrs:
            q = q.filter(SearchItem.search_attr.in_(attrs))

        # .all()
        return q
