from marshmallow import ValidationError

def content(value):
    if len(value) < 3:
        raise ValidationError('content min 3 character!')