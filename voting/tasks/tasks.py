from celery import Celery
import requests
from collections import Counter

app = Celery(__name__)

def encontrar_resultado_diferente(resultados):
    # Contar la frecuencia de cada resultado
    frecuencias = Counter(resultados)

    # Encontrar el resultado con frecuencia igual a 1 (el diferente)
    resultado_diferente = None
    for resultado, frecuencia in frecuencias.items():
        if frecuencia == 1: #o int(len(resultados)/2)
            resultado_diferente = resultado
            break

    return resultado_diferente

@app.task
def voting(resultados):

    resultados_filtrados = list(filter(lambda x: x["id"] == resultados[0]['id'], resultados))

    print(resultados_filtrados)

    if len(resultados_filtrados) >= 3:
        resultado_diferente = encontrar_resultado_diferente([res['Resultado'] for res in resultados_filtrados])
        
        if resultado_diferente is not None:
            print("Hay un resultado diferente:", resultado_diferente)
            # -
        else:
            print("Todos los resultados son iguales.")
    else:
        print("No hay suficientes resultados para verificar.")
 
        requests.delete("http://localhost:5002/rating/"+str(resultados[0]['id']))
