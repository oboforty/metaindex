from eme.data_access import RepositoryBase, Repository

from .entities import Comment


@Repository(Comment)
class CommentRepository(RepositoryBase):

    def list_for(self, entity_id, entity_type):
        return self.session.query(Comment)\
            .filter(Comment.entity_type == entity_type, Comment.entity_id == entity_id)\
        .all()
