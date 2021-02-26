from authlib.integrations.flask_oauth2 import current_token
from eme.data_access import get_repo
from flask import url_for, request

from modules.eme_utils.responses import ApiResponse
from modules.doors_oauth.services.auth import require_oauth
from modules.comments.dal.entities import Comment
from modules.comments.dal.repositories import CommentRepository


class CommentsApi:
    def __init__(self, server):
        self.server = server
        self.group = 'CommentsApi'
        self.route = ''

        self.server.preset_endpoints({
            'GET /api/<entity_type>/<entity_id>/comments': 'CommentsApi:get',
            'POST /api/<entity_type>/<entity_id>/comments': 'CommentsApi:post',
            #'PUT /api/<entity_type>/<entity_id>/comments': 'CommentsApi:put',
            'DELETE /api/<entity_type>/<entity_id>/comments': 'CommentsApi:delete',
        })

        self.repo: CommentRepository = get_repo(Comment)

    @require_oauth('profile')
    def get(self, entity_id, entity_type):
        comments = self.repo.list_for(entity_id, entity_type)

        return ApiResponse([comment.view for comment in comments])

    @require_oauth('profile')
    def post(self, entity_id, entity_type):
        content = request.json['content']
        parent_id = request.json['parent_id']

        comment = Comment(entity_id=entity_id, entity_type=entity_type, content=content, parent_id=parent_id)
        comment.author_id = current_token.user.uid

        self.repo.create(comment)

        return ApiResponse(comment.view_strict)

    @require_oauth('profile')
    def delete(self, comment_id):
        comment = self.repo.get(comment_id)

        self.repo.delete(comment)

        return ApiResponse({
        })
