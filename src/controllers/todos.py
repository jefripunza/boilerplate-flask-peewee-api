from flask import (
    request, g, jsonify
)
from apiflask import APIBlueprint
router = APIBlueprint('todos', __name__, tag='Todos')
from marshmallow import ValidationError

# =================================== #

from src.dto.todo import RequestTodoInsertUpdate
from src.middlewares.token import (token_validation_self)
from src.models.todos import Todos

# =================================== #

@router.route('/api/todo', methods=['GET', 'POST'])
@token_validation_self
def add_n_list_todos():
    user_id = g.user_id
    if request.method == 'POST':
        body = request.json
        schema = RequestTodoInsertUpdate()
        try:
            # Validate request body against schema data types
            body = schema.load(body)
        except ValidationError as err:
            # Return a nice message if validation fails
            return jsonify(err.messages), 400

        Todos.new_todo(content=body['content'], user_id=user_id)

        return jsonify(
            message='success insert todo!',
        )
    elif request.method == 'GET':
        list = Todos.list_todo_by_user_id(user_id=user_id)
        return jsonify(
            list=list,
        )

@router.route('/api/todo/<id>', methods=['PUT', 'DELETE'])
@token_validation_self
def edit_n_delete_todos(id):
    user_id = g.user_id
    is_exist = Todos.is_todo_exist(id, user_id)
    if not is_exist:
        return jsonify(
            message="todos id is not exist!",
        ), 400

    if request.method == 'PUT':
        body = request.json
        schema = RequestTodoInsertUpdate()
        try:
            # Validate request body against schema data types
            body = schema.load(body)
        except ValidationError as err:
            # Return a nice message if validation fails
            return jsonify(err.messages), 400

        Todos.update_todo_by_id(id=id, user_id=user_id, content=body['content'])

        return jsonify(
            message='success update todo!',
        )
    elif request.method == 'DELETE':
        Todos.delete_todo_by_id(id=id, user_id=user_id)

        return jsonify(
            message='success delete todo!',
        )

@router.route('/api/todo/done/<id>/<is_done>', methods=['PUT'])
@token_validation_self
def done_todos(id, is_done):
    user_id = g.user_id
    is_exist = Todos.is_todo_exist(id, user_id)
    if not is_exist:
        return jsonify(
            message="todos id is not exist!",
        ), 400

    if request.method == 'PATCH':
        Todos.done_todo_by_id(id=id, user_id=user_id, is_done=is_done == '1')

        return jsonify(
            message='success change done todo!',
        )