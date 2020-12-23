from eme.data_access import RepositoryBase, Repository

from ..dal.user import User


@Repository(User)
class UserRepository(RepositoryBase):

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
