from flask import (
    request, g, jsonify
)
from apiflask import APIBlueprint
from marshmallow import ValidationError

# =================================== #

from src.dto.todo import RequestTodoInsertUpdate
from src.middlewares.token import (token_validation_self)
from src.models.todos import Todos

# =================================== #

router = APIBlueprint('todos', __name__, tag='Todos')

@router.post('/api/todo')
@token_validation_self
@router.doc(security='Bearer')
def add_todos():
    user_id = g.user_id
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

@router.get('/api/todo')
@token_validation_self
@router.doc(security='Bearer')
def list_todos():
    user_id = g.user_id
    todos = Todos.list_todo_by_user_id(user_id=user_id)
    return jsonify(
        list=todos,
    )

@router.put('/api/todo/<id>')
@token_validation_self
@router.doc(security='Bearer')
def edit_todos(id):
    user_id = g.user_id
    is_exist = Todos.is_todo_exist(id, user_id)
    if not is_exist:
        return jsonify(
            message="todos id is not exist!",
        ), 400

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

@router.delete('/api/todo/<id>')
@token_validation_self
@router.doc(security='Bearer')
def delete_todos(id):
    user_id = g.user_id
    is_exist = Todos.is_todo_exist(id, user_id)
    if not is_exist:
        return jsonify(
            message="todos id is not exist!",
        ), 400

    Todos.delete_todo_by_id(id=id, user_id=user_id)
    return jsonify(
        message='success delete todo!',
    )

@router.patch('/api/todo/done/<id>/<is_done>')
@token_validation_self
@router.doc(security='Bearer')
def done_todos(id, is_done):
    user_id = g.user_id
    is_exist = Todos.is_todo_exist(id, user_id)
    if not is_exist:
        return jsonify(
            message="todos id is not exist!",
        ), 400

    Todos.done_todo_by_id(id=id, user_id=user_id, is_done=is_done == '1')
    return jsonify(
        message='success change done todo!',
    )