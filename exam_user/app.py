from examen_user import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
from celery import Celery

from examen_user import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
from celery import Celery
import uuid
import random

app = create_app('default')
celery = Celery(__name__, broker='redis://127.0.0.1:6379/0')
app_context = app.app_context()
app_context.push()
api = Api(app)
api.init_app(app)

@celery.task(name="test")
def enviar_examen(examen_json):
    pass


class VistaTest(Resource):

    def post(self):
        for i in range(0, 100):
            args=({
                "id": int(uuid.uuid4()),
                "Respuesta_1": random.randint(0, 50),
                "Respuesta_2": random.randint(0, 50),
                "falla": random.randint(0, 7)
            },)

            enviar_examen.apply_async(args)
        return "Enviados", 200

api.add_resource(VistaTest, '/test')