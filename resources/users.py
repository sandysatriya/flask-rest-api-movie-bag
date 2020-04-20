from flask import request, Response
from database.models import User
from flask_restful import Resource
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity


class UsersApi(Resource):
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)


class UserApi(Resource):
    @jwt_required
    def get(self, id):
        users = User.objects.get(id=id).to_json()
        return Response(users, mimetype="application/json", status=200)

    @jwt_required
    def put(self, id):
        # change password
        body = request.get_json()
        body.update({'password':
                     generate_password_hash(body['password']).decode('utf8')})
        users = User.objects.get(id=id).update(**body)
        return {'data': users}
