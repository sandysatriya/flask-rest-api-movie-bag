from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)
initialize_routes(api)

# app.register_blueprint(movies)


# movie = []

# @app.route('/movies', methods=['POST'])
# def add_movie():
#     movie = request.get_json()
#     movies.append(movie)
#     return {
#         'id': len(movies),
#         'data': movies
#     }, 200


# @app.route('/movies/<int:index>', methods=['PUT'])
# def update_movie(index):
#     try:
#         movie = request.get_json()
#         movies[index] = movie
#         return jsonify(movies[index]), 200
#     except Exception as e:
#         return {'message': str(e)}, 404

# @app.route('/movies/<int:index>', methods=['DELETE'])
# def delete_movie(index):
#     movies.pop(index)
#     return {'message': 'Success Delete'}, 200

app.run()
