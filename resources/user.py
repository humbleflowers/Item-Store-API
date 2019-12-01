import sqlite3
from flask_restful import Resource, Api, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str, required=True,
                        help="Username")
    parser.add_argument('password',
                        type=str, required=True,
                        help='Password')
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already present'.format(data['username'])}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {'message':'User {} created successfully'.format(data['username'])}, 201

