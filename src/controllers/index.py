from flask import (
    Blueprint, jsonify
)

# =================================== #

router = Blueprint('index', __name__)

@router.get('/')
def root():
    return jsonify(
        message="welcome...",
    )
