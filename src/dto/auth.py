from marshmallow import Schema, fields

class RequestRegister(Schema):
    name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    role = fields.String(required=True)

class RequestLogin(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)