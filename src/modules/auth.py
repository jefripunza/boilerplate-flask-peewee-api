from flask import (
    request, g, jsonify, make_response
)
from apiflask import APIBlueprint
from marshmallow import ValidationError

# =================================== #

from config import role_user
from src.utils.JWT import create_token

from src.dto.auth import RequestRegister, RequestLogin
from src.dto.basic import ResponseMessageOnly

from src.models.users import Users

# =================================== #

router = APIBlueprint('auth', __name__, tag="Auth")

@router.post('/api/auth/v1/register')
@router.input(RequestRegister, example={
    'name': 'Jefri Herdi Triyanto',
    'username': 'jefripunza',
    'password': 'adaajadeh',
    'role': 'buyer',
})
@router.output(ResponseMessageOnly, 200)
@router.output(ResponseMessageOnly, 400)
def register(body):
    schema = RequestRegister()
    try:
        # Validate request body against schema data types
        body = schema.load(body)
    except ValidationError as err:
        # Return a nice message if validation fails
        return make_response(jsonify(err.messages), 405)

    if body['role'] not in role_user:
        return make_response(jsonify(
            message="role cannot permit to register!",
        ), 400)

    is_username_exist = Users.is_username_exist(body['username'])
    if is_username_exist:
        return make_response(jsonify(
            message='username is exist!',
        ), 400)

    Users.new_user(name=body['name'], username=body['username'], password=body['password'], role=body['role'])

    return make_response(jsonify(
        message="success register!",
    ))

@router.post('/api/auth/v1/login')
@router.input(RequestLogin,  example={
    'username': 'jefripunza',
    'password': 'adaajadeh',
})
@router.output(ResponseMessageOnly, 200)
@router.output(ResponseMessageOnly, 400)
def login(self):
    body = request.json
    schema = RequestLogin()
    try:
        # Validate request body against schema data types
        body = schema.load(body)
    except ValidationError as err:
        # Return a nice message if validation fails
        return make_response(jsonify(err.messages), 405)

    is_login = Users.is_login(username=body['username'], password=body['password'])
    if not is_login:
        return make_response(jsonify(
            message="username or password wrong!",
        ), 400)

    g.is_jwt_expired = False
    return make_response(jsonify(
        token = create_token(id=is_login.id, role=is_login.role),
    ))
