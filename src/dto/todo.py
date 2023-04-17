from marshmallow import Schema, fields

from src.dto.validations.todo import \
    content as validation_content

class RequestTodoInsert(Schema):
    content = fields.String(required=True, validate=validation_content)

class RequestTodoUpdate(Schema):
    content = fields.String(required=False, validate=validation_content)
