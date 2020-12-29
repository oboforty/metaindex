from time import time

from eme.data_access import RepositoryBase, Repository

from ..dal.user import User


@Repository(User)
class UserRepository(RepositoryBase):

    def find_by_token(self, token):
        return self.session.query(User)\
            .filter(User.access_token == token)\
        .first()

    def delete_inactive(self, inactive_for=14*24*3600):
        self.session.query(User)\
            .filter(User.last_active + inactive_for < time())\
        .delete(synchronize_session=False)
        self.session.commit()

    def create(self, ent, commit=True):
        user = self.session.query(User).filter(User.uid == ent.uid).first()
        if user is not None:
            self.session.delete(user)
            self.session.commit()

        super().create(ent, commit)

    def find_user(self, uid=None, email=None, username=None, code=None):
        if uid is not None:
            return self.get(uid)

        sq = self.session.query(self.T)

        if username is not None:
            sq = sq.filter(self.T.username == username)
        elif email is not None:
            sq = sq.filter(self.T.email == email)
        elif code is not None:
            sq = sq.filter(self.T.forgot_code == code)
        else:
            return None

        return sq.first()

    def list_some(self, N):
        return self.session.query(User)\
            .limit(N)\
        .all()

    def delete_all_test(self):
        self.session.query(User)\
            .filter(User.username.like('___TEST___%'))\
        .delete(synchronize_session=False)
        self.session.commit()
