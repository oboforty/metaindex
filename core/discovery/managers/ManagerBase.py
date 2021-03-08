from abc import abstractmethod, ABCMeta

from core.dal import MetaboliteDataRepositoryBase, MetaboliteView
from core.discovery.utils import merge_attr


class ManagerBase(metaclass=ABCMeta):
    name: str
    padding: str = None

    _select: tuple
    _reverse: tuple
    _remap: dict = {}

    repo: MetaboliteDataRepositoryBase

    @abstractmethod
    def fetch_api(self, db_id):
        pass

    def query_primary(self, db_id) -> MetaboliteView:
        db_data = self.repo.get(self.depad_id(db_id))

        if db_data is None:
            # not found
            return None

        mv = MetaboliteView()
        mv.meta_id = None

        for attr in self._select:
            dbval = getattr(db_data, attr)

            mattr = self._remap.get(attr, attr)

            # set multi value:
            merge_attr(mv, mattr, dbval)

        return mv

    def query_reverse(self, df_disc):
        q = self.repo.select()
        T = self.repo.T

        for attr in self._reverse:
            q = q.filter(getattr(T, attr) == getattr(df_disc, attr))

        return q.all()

    def save(self, db_id, df_result):
        self.repo.create(df_result)

    def query_multiple(self, db_ids: list):
        return self.repo.list(db_ids)

    # def resolve_secondary_id(self, db_id: str):
    #     # todo: yeah
    #     pass

    def pad_id(self, db_id: str):
        if self.padding != None and db_id[0:4].lower() != self.padding.lower():
            return self.padding+db_id
        return db_id

    def depad_id(self, db_id: str):
        if self.padding != None and db_id.startswith(self.padding):
            return db_id[len(self.padding):]
        return db_id
