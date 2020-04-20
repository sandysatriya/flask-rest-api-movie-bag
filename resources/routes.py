from .movie import *
from .auth import *
from .users import *


def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')

    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/users/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
