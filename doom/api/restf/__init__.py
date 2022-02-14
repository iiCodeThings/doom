from flask_restful import Api


from .api import UserLoginResource


restf_api = Api(prefix='/restf', default_mediatype='application/json')
restf_api.add_resource(UserLoginResource, '/user/login')

