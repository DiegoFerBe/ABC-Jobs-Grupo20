from celery import Celery
import requests
from .info import microservice_name
import datetime


app = Celery('tasks2', broker='redis://127.0.0.1:6379/0')

@app.task(name="tasks2_enviar_examen")
def tasks2_enviar_examen(examen_json):
    examen = examen_json
    examen["identificador_servicio"] = microservice_name
    if microservice_name.rsplit("-", 1)[1] == str(examen["falla"]):
        examen["Resultado"] = 0
    else:
        examen["Resultado"] = examen["Respuesta_1"] + examen["Respuesta_2"]
    
    examen["enviado"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    requests.post("http://localhost:5002/ratings", json=examen)
