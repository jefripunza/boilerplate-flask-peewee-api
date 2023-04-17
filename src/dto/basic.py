from apiflask import Schema
from apiflask.fields import String

class ResponseMessageOnly(Schema):
    message = String()
