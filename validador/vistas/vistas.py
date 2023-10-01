

from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
import datetime
from flask_jwt_extended.view_decorators import jwt_required

class User(Resource):

    def post(self):

        access = create_access_token(identity='diego',
                expires_delta=datetime.timedelta(minutes=60),)

        return access

class ProfessionalSelection(Resource):
    @jwt_required()
    def get(self):


        return 'Test'