from eme.data_access import RepositoryBase


class MetaboliteDataRepositoryBase(RepositoryBase):
    primary_id = None

    def get_first(self):
        return self.session.query(self.T).first()

    def list(self, _ids: list):
        return self.session.query(self.T)\
            .filter(self.primary_id.in_(_ids))\
            .all()
