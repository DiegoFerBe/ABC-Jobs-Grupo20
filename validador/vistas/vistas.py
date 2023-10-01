from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt
import datetime
from flask_jwt_extended.view_decorators import jwt_required
import random

class User(Resource):

    def post(self):

        num = random.randint(0, 1)

        if num == 0:
            role = "admin"
        else:
            role = "user"

        access = create_access_token(identity='diego',
                expires_delta=datetime.timedelta(minutes=60),
                additional_claims={"rol": role},)

        return {'token':access,'rol':role}, 200
    

class ViewVoting(Resource):
    @jwt_required()
    def get(self):

        claims = get_jwt()
        if claims["rol"] == "admin":
            return Response(response="Acceso permitido", status=200)
        else:
            return Response(response="No autorizado", status=401)

