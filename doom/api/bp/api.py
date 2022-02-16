from flask import request
from . import api_blueprint


@api_blueprint.route('/test', methods=['GET'])
def api_blueprint_test():
    return "api blueprint"
