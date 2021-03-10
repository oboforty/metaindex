from abc import abstractmethod, ABCMeta

from core.dal import MetaboliteDataRepositoryBase, MetaboliteView
from core.discovery.utils import merge_attr, depad_id, pad_id


class ManagerBase(metaclass=ABCMeta):
    name: str
    padding: str = None

    _select: tuple
    _reverse: tuple
    _remap: dict = {}

    repo: MetaboliteDataRepositoryBase

    def get_metabolite(self, db_id, cache=True):
        """
        Fetches record from cache or public API
        """
        db_tag = self.repo.primary_id
        db_data = self.repo.get(depad_id(db_id, db_tag))

        if not db_data:
            # fetch public API in case the data record wasn't found
            print("API")
            db_data = self.fetch_api(pad_id(db_id, db_tag), meta_view=False)

            if db_data and cache:
                self.repo.create(db_data)

        # transform data to common interface
        return self.to_view(db_data)

    def query_primary(self, db_id, meta_view: bool = True) -> MetaboliteView:
        db_tag = self.repo.primary_id
        db_data = self.repo.get(depad_id(db_id, db_tag))

        return self.to_view(db_data) if meta_view else db_data

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
    def fetch_api(self, db_id, meta_view: bool = True):
        pass

    def to_view(self, db_data) -> MetaboliteView:
        """
            Converts [DB]Data into generalized Metabolite view
        """
        if db_data is None:
            return None

        mv = MetaboliteView()
        mv.meta_id = None

        for attr in self._select:
            dbval = getattr(db_data, attr)

            mattr = self._remap.get(attr, attr)

            # set multi value:
            merge_attr(mv, mattr, dbval)

        return mv
