from time import time

from eme.data_access import Repository, RepositoryBase

from core.dal.user import User


@Repository(User)
class UserRepository(RepositoryBase):

    def set_world(self, uid, wid, iso, commit=True):
        self.session.query(User)\
            .filter(User.uid == uid)\
            .update({User.wid: wid, User.iso: iso})

        if commit:
            self.session.commit()

    def find_by_iso(self, iso, wid):
        return self.session.query(User)\
            .filter(User.wid == wid, User.iso == iso)\
        .first()

    def list_all(self, wid=None):
        if wid:
            return self.session.query(User) \
                .filter(User.wid == wid)
        else:
            return self.session.query(User)

    def list_names(self, wid=None):
        return self.session.query(User.iso, User.username, User.uid) \
            .filter(User.wid == wid) \
            .all()

    def transfer_to(self, wid1, wid2, commit=True):
        """
        Transfer users from one world into another
        :param wid1: from world
        :param wid2: to world
        :param commit: wether to commit automatically
        """

        self.session.query(User)\
            .filter(User.wid == wid1)\
            .update({User.wid: wid2})

        if commit:
            self.session.commit()

    def list_some(self, N):
        return self.session.query(User)\
            .limit(N)\
        .all()

    def find_by_username(self, username):
        return self.session.query(User)\
            .filter(User.username == username)\
        .first()

    def find_by_token(self, token):
        return self.session.query(User)\
            .filter(User.access_token == token)\
        .first()

    def delete_inactive(self):
        self.session.query(User)\
            .filter(User.last_active + 14*24*3600 < time())\
        .delete(synchronize_session=False)
        self.session.commit()

    def create(self, ent, commit=True):
        user = self.session.query(User).filter(User.uid == ent.uid).first()
        if user is not None:
            self.session.delete(user)
            self.session.commit()

        super().create(ent, commit)
