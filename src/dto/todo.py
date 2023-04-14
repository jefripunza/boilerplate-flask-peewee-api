from marshmallow import Schema, fields

class RequestTodoInsertUpdate(Schema):
    content = fields.String(required=True)
