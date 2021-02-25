from eme.data_access import Repository, RepositoryBase

from ..entities.user import User
from modules.doors_oauth import UserRepositoryBase


@Repository(User)
class UserRepository(UserRepositoryBase):
    pass
