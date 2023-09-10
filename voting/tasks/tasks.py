from celery import Celery
import requests

app = Celery(__name__)

@app.task
def voting(resultados):

    resultados_filtrados = list(filter(lambda x: x["id"] == resultados[0]['id'], resultados))

    print(resultados_filtrados)

    if len(resultados_filtrados) >= 3:
        # primer_resultado = None
        # for objeto in resultados_filtrados:
        #     resultado_actual = objeto["Resultado"]
        #     if primer_resultado is None:
        #         primer_resultado = resultado_actual
        #     elif resultado_actual != primer_resultado:
        #         segundo_resultado = objeto
        #         break
        #     elif segundo_resultado == resultado_actual:
        #         objeto_diferente = primer_resultado
        # print("Servicio fallando",objeto_diferente)
 
        requests.delete("http://localhost:5002/rating/"+str(resultados[0]['id']))
