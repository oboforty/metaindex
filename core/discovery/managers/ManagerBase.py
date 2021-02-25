from abc import abstractmethod, ABCMeta

from core.dal.base.meta_repo import MetaboliteDataRepositoryBase


class ManagerBase(metaclass=ABCMeta):
    name: str
    repo: MetaboliteDataRepositoryBase

    @abstractmethod
    def fetch_api(self, db_id):
        pass

    @abstractmethod
    def query_primary(self, db_id):
        pass

    @abstractmethod
    def query_reverse(self, db_id):
        pass

    def query_multiple(self, db_ids: list):
        return self.repo.list(db_ids)

    def resolve_secondary_id(self, db_id: str):
        # todo: yeah
        pass
