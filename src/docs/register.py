from apiflask import Schema
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf

from config import role_user

class DocRequestRegister(Schema):
    name = String(required=True, description='fullname user.')
    username = String(required=True, description='key for auth login.')
    password = String(required=True, validate=Length(min=8, max=30), description='credential for login.')
    role = String(required=True, validate=OneOf(role_user), description='for permission issue.')