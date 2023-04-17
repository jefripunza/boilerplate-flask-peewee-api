from marshmallow import Schema, fields

from src.dto.validations.product_categories import \
    name as validation_name

class RequestProductCategoriesInsert(Schema):
    name = fields.String(required=True, validate=validation_name)

class RequestProductCategoriesUpdate(Schema):
    name = fields.String(required=False, validate=validation_name)
