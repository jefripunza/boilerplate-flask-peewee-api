from flask import (
    Blueprint, jsonify, make_response
)

# =================================== #

router = Blueprint('index', __name__)

@router.get('/')
def root():
    return make_response(jsonify(
        message="welcome...",
    ))
