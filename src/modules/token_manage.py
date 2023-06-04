from flask import (
    g, jsonify, make_response
)
from apiflask import APIBlueprint

# =================================== #

from src.middlewares.token import (token_validation_self, token_validation)
from src.utils.JWT import create_token

# =================================== #

router = APIBlueprint('token', __name__, tag='Token')

from src import app
@app.after_request
def handle_refresh_token(response):
    try:
        # self
        if g.is_jwt_expired is not None and g.is_jwt_expired == True:
            response.headers['X-New-Token'] = create_token(id=g.user_id, role=g.user_role)

        # service
        if g.jwt_refresh_token is not None and g.jwt_refresh_token != False:
            response.headers['X-New-Token'] = g.jwt_refresh_token
    except:
        return response
    return response

# =================================== #

@router.get('/api/token/validation')
@token_validation_self
@router.doc(security='Bearer')
def self_process():
    return make_response(jsonify(
        id=g.user_id,
        role=g.user_role,
    ))


@router.get('/api/token/validation-service')
@token_validation
@router.doc(security='Bearer')
def microservice_process():
    return make_response(jsonify(
        id= g.user_id,
        role= g.user_role,
    ))
