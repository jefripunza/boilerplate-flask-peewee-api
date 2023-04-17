from marshmallow import ValidationError

from config import role_user

def name(value):
    if len(value) < 3:
        raise ValidationError('name min 3 character!')

def username(value):
    if len(value) < 5:
        raise ValidationError('username min 5 character!')
    if len(value) >= 20:
        raise ValidationError('username max 10 character!')

def password(value):
    if len(value) < 8:
        raise ValidationError('password min 8 character!')
    if len(value) >= 30:
        raise ValidationError('password max 30 character!')

def role(value):
    print(value)
    if value not in role_user:
        raise ValidationError('role are not allowed!')

