from marshmallow import ValidationError

def name(value):
    if len(value) < 3:
        raise ValidationError('name category min 3 character!')