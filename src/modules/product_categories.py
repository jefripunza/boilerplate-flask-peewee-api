from flask import (
    request, g, jsonify, make_response
)
from apiflask import APIBlueprint
from marshmallow import ValidationError

# =================================== #

from src.dto.product_categories import RequestProductCategoriesInsert, RequestProductCategoriesUpdate
from src.dto.basic import ResponseMessageOnly

from src.middlewares.token import (token_validation_self)
from src.middlewares.user_validation import (is_admin)
from src.models.products import ProductCategories

# =================================== #

router = APIBlueprint('product_categories', __name__, tag='Product Categories')

@router.post('/api/product-category')
@token_validation_self
@is_admin
@router.doc(security='Bearer')
@router.input(RequestProductCategoriesInsert, example={
    'name': 'Elektronik',
})
@router.output(ResponseMessageOnly, 200)
@router.output(ResponseMessageOnly, 400)
def add_category(body):
    user_id = g.user_id
    schema = RequestProductCategoriesInsert()
    try:
        # Validate request body against schema data types
        body = schema.load(body)
    except ValidationError as err:
        # Return a nice message if validation fails
        return make_response(jsonify(err.messages), 405)

    is_exist = ProductCategories.is_exist(name=body['name'])
    if is_exist:
        return make_response(jsonify(
            message="category name is exist!",
        ), 400)

    ProductCategories.new(name=body['name'], created_by=user_id)
    return make_response(jsonify(
        message='success insert category!',
    ))

@router.get('/api/product-category')
def list_categories():
    categories = ProductCategories.show_all()
    return make_response(jsonify(
        list=categories,
    ))

@router.put('/api/product-category/<id>')
@token_validation_self
@is_admin
@router.doc(security='Bearer')
@router.input(RequestProductCategoriesUpdate, example={
    'name': 'Handphone',
})
@router.output(ResponseMessageOnly, 200)
@router.output(ResponseMessageOnly, 400)
def edit_category(id, body):
    is_exist = ProductCategories.is_exist_by_id(id)
    if not is_exist:
        return make_response(jsonify(
            message="category id is not exist!",
        ), 400)

    schema = RequestProductCategoriesUpdate()
    try:
        # Validate request body against schema data types
        body = schema.load(body)
    except ValidationError as err:
        # Return a nice message if validation fails
        return make_response(jsonify(err.messages), 405)

    is_exist = ProductCategories.is_exist(name=body['name'])
    if is_exist:
        return make_response(jsonify(
            message="category name is exist!",
        ), 400)

    ProductCategories.update_by_id(id=id, name=body['name'])
    return make_response(jsonify(
        message='success update category!',
    ))

@router.patch('/api/product-category/show/<id>/<is_show>')
@token_validation_self
@is_admin
@router.doc(security='Bearer')
@router.output(ResponseMessageOnly, 200)
@router.output(ResponseMessageOnly, 400)
def done_todos(id, is_show):
    is_exist = ProductCategories.is_exist_by_id(id)
    if not is_exist:
        return make_response(jsonify(
            message="category id is not exist!",
        ), 400)

    ProductCategories.show_by_id(id=id, is_show=is_show == '1')
    return make_response(jsonify(
        message='success change show category!',
    ))

