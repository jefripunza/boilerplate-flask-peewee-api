from apiflask import Schema
from apiflask.fields import String

class DocResponseMessageOnly(Schema):
    message = String()
