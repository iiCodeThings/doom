from flask_restful import reqparse
from doom.api.restf.resource import BaseResource


class UserLoginResource(BaseResource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True,
                            location='json', help='username is required')
        parser.add_argument('password', type=str, required=True,
                            location='json', help='password is required')
        args = parser.parse_args()
        return self.build_response(self.OK, {'u': args.username, 'p': args.password})
