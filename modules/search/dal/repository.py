from eme.data_access import Repository, RepositoryBase

from modules.search.dal.entity import SearchItem


@Repository(SearchItem)
class SearchItemRepository(RepositoryBase):
    pass