from eme.data_access import Repository, RepositoryBase
from sqlalchemy import and_, func

from core.dal.world import World
from core.dal.user import User


@Repository(World)
class WorldRepository(RepositoryBase):

    def get_first(self):
        return self.session.query(World).first()

    def find_by_invite(self, invlink):
        return self.session.query(World)\
            .filter(World.invlink == invlink)\
        .first()

    def list_inactive(self):
        # todo: this is not working lol
        # return self.session.query(World)\
        #     .filter(World.invlink == invlink)\
        # .first()
        pass

    def delete_unoccupied(self):
        return self.session.query(World) \
            .outerjoin(User, User.wid == World.wid) \
            .group_by(World.wid) \
            .having(func.count(User.uid) == 0)\
            .delete()
