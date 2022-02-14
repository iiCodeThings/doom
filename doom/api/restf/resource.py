import json
from flask import make_response
from flask_restful import Resource


class ErrorCode(object):

    OK = (0, "OK")


class BaseResource(ErrorCode, Resource):

    def build_response(self, err_code, data=None):
        params = {
            'meta': {
                'code': err_code[0],
                'message': err_code[1]
            },
            'data': data
        }
        response = make_response(json.dumps(data))
        response.headers['Content-Type'] = 'application/json'
        return response
