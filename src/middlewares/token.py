from flask import request, g, jsonify, make_response
from functools import wraps

import jwt
from config import AUTH_SERVICE
from src.utils.JWT import token_validate, check_expired
def token_validation_self(f):
    @wraps(f)
    def _next(*args, **kwargs):
        token = request.headers.get('authorization')
        if not token or not token.startswith('Bearer '):
            return make_response(jsonify(
                message='Authorization Bearer is required!',
            ), 403)
        try:
            token = token.split(' ')[1]
            g.is_jwt_expired = False
            result = token_validate(token=token)
            is_expired = check_expired(exp=result['exp'])
            if is_expired:
                g.is_jwt_expired = True
            g.user_id = result['id']
            g.user_role = result['role']
        except Exception as e:
            return make_response(jsonify(
                message= str(e) + "!",
            ), 401)
        # next...
        return f(*args, **kwargs)
    return _next

import requests
def token_validation(f):
    @wraps(f)
    def _next(*args, **kwargs):
        token = request.headers.get('authorization')
        if not token or not token.startswith('Bearer '):
            return make_response(jsonify(
                message='Authorization Bearer is required!',
            ), 403)
        try:
            g.is_jwt_expired = False
            g.jwt_refresh_token = None
            result = requests.get('%s/api/token/validation' % AUTH_SERVICE, headers = {
                "authorization": token,
            })
            refresh_token = result.headers.get("x-new-token")
            response = result.json()
            if result.status_code != 200:
                return make_response(jsonify(
                    message= response['message'],
                ), result.status_code)
            g.user_id = response['id']
            g.user_role = response['role']
            g.is_jwt_expired = True if refresh_token else False
            g.jwt_refresh_token = refresh_token if g.is_jwt_expired else None
        except Exception as e:
            return make_response(jsonify(
                message= str(e) + "!",
            ), 401)
        # next...
        return f(*args, **kwargs)
    return _next