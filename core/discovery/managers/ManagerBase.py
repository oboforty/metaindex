from abc import abstractmethod, ABCMeta

from core.dal import MetaboliteDataRepositoryBase, MetaboliteView
from core.discovery.utils import merge_attr, depad_id


class ManagerBase(metaclass=ABCMeta):
    name: str
    padding: str = None

    _select: tuple
    _reverse: tuple
    _remap: dict = {}

    repo: MetaboliteDataRepositoryBase

    def get_metabolite(self, db_id):
        """
        Fetches record from cache or public API
        """

        cached = self.query_primary(db_id)

        if not cached:

            self.fetch_api(db_id)

            print("TDOO")

        #
        # def save(self, db_id, df_result):
        #     self.repo.create(df_result)

        # @abstractmethod
        # def fetch_api(self, db_id):
        #     pass
        #
        # # call API
        # if not df_result:
        #     df_result = hand.fetch_api(db_id)
        #
        #     if df_result:
        #         hand.save(db_id, df_result)

    def query_primary(self, db_id) -> MetaboliteView:
        db_data = self.repo.get(depad_id(db_id, self.repo.primary_id))

        if db_data is None:
            # not found
            return None

        return self.to_view(db_data)

    def query_reverse(self, df_disc):
        q = self.repo.select()
        T = self.repo.T

        for db_tag in self._reverse:
            search_val = getattr(df_disc, db_tag)

            if not search_val:
                # skip where clause if there's no value to reverse query by
                continue

            if isinstance(search_val, (set, list, tuple)):
                # SQL IN
                search_val = set(map(lambda x: depad_id(x, db_tag), search_val))
                q = q.filter(getattr(T, db_tag).in_(search_val))
            else:
                # scalar WHERE
                search_val = depad_id(search_val, db_tag)
                q = q.filter(getattr(T, db_tag) == search_val)

        return q.all()

    def query_multiple(self, db_ids: list):
        return self.repo.list(db_ids)

    def resolve_secondary_id(self, db_id: str):
        # todo: yeah
        pass

    @abstractmethod
    def fetch_api(self, db_id, save_cached=True):
        pass

    def to_view(self, db_data) -> MetaboliteView:
        """
            Converts [DB]Data into generalized Metabolite view
        """
        mv = MetaboliteView()
        mv.meta_id = None

        for attr in self._select:
            dbval = getattr(db_data, attr)

            mattr = self._remap.get(attr, attr)

            # set multi value:
            merge_attr(mv, mattr, dbval)

        return mv
