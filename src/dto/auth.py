from marshmallow import Schema, fields

from src.dto.validations.user import \
    name as validate_name, \
    username as validate_username, \
    password as validate_password, \
    role as validate_role

class RequestRegister(Schema):
    name = fields.String(required=True, validate=validate_name)
    username = fields.String(required=True, validate=validate_username)
    password = fields.String(required=True, validate=validate_password)
    role = fields.String(required=True, validate=validate_role)

class RequestLogin(Schema):
    username = fields.String(required=True, validate=validate_username)
    password = fields.String(required=True, validate=validate_password)