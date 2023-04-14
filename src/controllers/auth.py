from flask import (
    request, g, jsonify
)
from apiflask import APIBlueprint
router = APIBlueprint('auth', __name__, tag="Auth")
from marshmallow import ValidationError

from config import role_register
from src.modules.JWT import create_token

# =================================== #

from src.dto.auth import RequestRegister, RequestLogin
from src.models.users import Users

# =================================== #

@router.route('/api/auth/v1/register', methods=['POST'])
def register():
    body = request.json
    schema = RequestRegister()
    try:
        # Validate request body against schema data types
        body = schema.load(body)
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400

    if body['role'] not in role_register:
        return jsonify(
            message="role cannot permit to register!",
        ), 400

    is_username_exist = Users.is_username_exist(body['username'])
    if is_username_exist:
        return jsonify(
            message="username is exist!",
        ), 400

    Users.new_user(name=body['name'], username=body['username'], password=body['password'], role=body['role'])

    return jsonify(
        message="success register!",
    )

@router.route('/api/auth/v1/login', methods=['POST'])
def login():
    body = request.json
    schema = RequestLogin()
    try:
        # Validate request body against schema data types
        body = schema.load(body)
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400

    is_login = Users.is_login(username=body['username'], password=body['password'])
    if not is_login:
        return jsonify(
            message="username or password wrong!",
        ), 400

    g.is_jwt_expired = False
    return jsonify(
        token = create_token(id=is_login.id, role=is_login.role),
    )
