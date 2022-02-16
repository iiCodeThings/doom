from flask import Blueprint


api_blueprint = Blueprint('api', __name__, url_prefix='/api/1.0')

from .api import api_blueprint_test
