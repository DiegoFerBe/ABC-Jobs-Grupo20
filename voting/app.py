from examiner import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from celery import Celery
from .tasks import voting
import requests
import json


app = create_app('default')
app_context = app.app_context()
app_context.push()
api = Api(app)
api.init_app(app)

resultados = []

class VistaRatings(Resource):

    def post(self):
        rating = request.get_json()
        resultados.append(rating)
        if len(resultados) >= 3:
            args = (resultados,)
            voting.apply(args)
        return resultados, 200
    
    def get(self):
        return resultados, 200
    

class VistaRating(Resource):

    def delete(self, id):
        global resultados
        resultados = list(filter(lambda x: x["id"] == id, resultados))
        return '', 204
        

api.add_resource(VistaRatings, '/ratings')
api.add_resource(VistaRating, '/rating/<int:id>')