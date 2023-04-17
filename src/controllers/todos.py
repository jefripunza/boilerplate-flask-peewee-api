from flask import (
    request, g, jsonify, make_response
)
from apiflask import APIBlueprint
from marshmallow import ValidationError

# =================================== #

from src.dto.todo import RequestTodoInsert, RequestTodoUpdate
from src.dto.basic import ResponseMessageOnly

from src.middlewares.token import (token_validation_self)
from src.models.todos import Todos

# =================================== #

router = APIBlueprint('todos', __name__, tag='Todos')

@router.post('/api/todo')
@token_validation_self
@router.doc(security='Bearer')
@router.input(RequestTodoInsert, example={
    'content': 'testing...',
})
@router.output(ResponseMessageOnly, 200)
@router.output(ResponseMessageOnly, 400)
def add_todos(body):
    user_id = g.user_id
    schema = RequestTodoInsert()
    try:
        # Validate request body against schema data types
        body = schema.load(body)
    except ValidationError as err:
        # Return a nice message if validation fails
        return make_response(jsonify(err.messages), 405)

    Todos.new(content=body['content'], user_id=user_id)
    return make_response(jsonify(
        message='success insert todo!',
    ))

@router.get('/api/todo')
@token_validation_self
@router.doc(security='Bearer')
def list_todos():
    user_id = g.user_id
    todos = Todos.list_by_user_id(user_id=user_id)
    return make_response(jsonify(
        list=todos,
    ))

@router.put('/api/todo/<id>')
@token_validation_self
@router.doc(security='Bearer')
@router.input(RequestTodoUpdate, example={
    'content': 'testing aja...',
})
@router.output(ResponseMessageOnly, 200)
@router.output(ResponseMessageOnly, 400)
def edit_todos(id, body):
    user_id = g.user_id
    is_exist = Todos.is_exist(id, user_id)
    if not is_exist:
        return make_response(jsonify(
            message="todos id is not exist!",
        ), 400)

    schema = RequestTodoUpdate()
    try:
        # Validate request body against schema data types
        body = schema.load(body)
    except ValidationError as err:
        # Return a nice message if validation fails
        return make_response(jsonify(err.messages), 405)

    Todos.update_by_id(id=id, user_id=user_id, content=body['content'])
    return make_response(jsonify(
        message='success update todo!',
    ))

@router.patch('/api/todo/done/<id>/<is_done>')
@token_validation_self
@router.doc(security='Bearer')
@router.output(ResponseMessageOnly, 200)
@router.output(ResponseMessageOnly, 400)
def done_todos(id, is_done):
    user_id = g.user_id
    is_exist = Todos.is_exist(id, user_id)
    if not is_exist:
        return make_response(jsonify(
            message="todos id is not exist!",
        ), 400)

    Todos.done_by_id(id=id, user_id=user_id, is_done=is_done == '1')
    return make_response(jsonify(
        message='success change done todo!',
    ))

@router.delete('/api/todo/<id>')
@token_validation_self
@router.doc(security='Bearer')
@router.output(ResponseMessageOnly, 200)
@router.output(ResponseMessageOnly, 400)
def delete_todos(id):
    user_id = g.user_id
    is_exist = Todos.is_exist(id, user_id)
    if not is_exist:
        return make_response(jsonify(
            message="todos id is not exist!",
        ), 400)

    Todos.delete_by_id(id=id, user_id=user_id)
    return make_response(jsonify(
        message='success delete todo!',
    ))
