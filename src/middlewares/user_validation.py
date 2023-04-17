from flask import g, jsonify, make_response
from functools import wraps

# ==================================================================================================================== #

def is_superadmin(f):
    @wraps(f)
    def _next(*args, **kwargs):
        role = g.user_role
        if role not in ['superadmin']:
            return make_response(jsonify(
                message="only superadmin!",
            ), 401)
        # next...
        return f(*args, **kwargs)
    return _next

def is_admin(f):
    @wraps(f)
    def _next(*args, **kwargs):
        role = g.user_role
        if role not in ['superadmin', 'admin']:
            return make_response(jsonify(
                message="only admin!",
            ), 401)
        # next...
        return f(*args, **kwargs)
    return _next

# ==================================================================================================================== #

def is_merchant(f):
    @wraps(f)
    def _next(*args, **kwargs):
        role = g.user_role
        if role not in ['superadmin', 'merchant']:
            return make_response(jsonify(
                message="only merchant!",
            ), 401)
        # next...
        return f(*args, **kwargs)
    return _next

def is_buyer(f):
    @wraps(f)
    def _next(*args, **kwargs):
        role = g.user_role
        if role not in ['superadmin', 'buyer']:
            return make_response(jsonify(
                message="only buyer!",
            ), 401)
        # next...
        return f(*args, **kwargs)
    return _next
