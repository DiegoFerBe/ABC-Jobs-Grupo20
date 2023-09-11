from celery import Celery
import requests
from collections import Counter
import datetime
import csv


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

def voting(resultados):

    #print("Resultados:", resultados)

    resultados_filtrados = list(filter(lambda x: x["id"] == resultados[0]['id'], resultados))

    #print(resultados_filtrados)

    if len(resultados_filtrados) >= 3:
        resultado_diferente = encontrar_resultado_diferente(resultados_filtrados)

        print("Resultado diferente:",resultado_diferente[0])
        print("Resultado correcto:",resultado_diferente[1])

        if resultado_diferente[0] is None:
            resultado_voting={
                "id": resultado_diferente[1]['id'],
                "respuesta_1": resultado_diferente[1]['Respuesta_1'],
                "respuesta_2": resultado_diferente[1]['Respuesta_2'],
                "resultado": resultado_diferente[1]['Resultado'],
                "hora_examiner": resultado_diferente[1]['enviado'],
                "hora_voting": datetime.datetime.now(),
                "falla_esperada": resultado_diferente[1]['falla'],
                "falla_obtenida": 'Ninguna',
                
            }
        else:
            resultado_voting={
                "id": resultado_diferente[1]['id'],
                "respuesta_1": resultado_diferente[1]['Respuesta_1'],
                "respuesta_2": resultado_diferente[1]['Respuesta_2'],
                "resultado": resultado_diferente[1]['Resultado'],
                "hora_examiner": resultado_diferente[1]['enviado'],
                "hora_voting": datetime.datetime.now(),
                "falla_esperada": resultado_diferente[1]['falla'],
                "falla_obtenida": resultado_diferente[0]['identificador_servicio'],
                
            }
        
        # Ruta del archivo CSV donde deseas guardar el diccionario
        archivo_csv = "datos.csv"
# Abrir el archivo CSV en modo de escritura
        with open(archivo_csv, mode="a", newline="") as file:
    # Crear un objeto escritor CSV
            writer = csv.DictWriter(file, fieldnames=resultado_voting.keys())
    # Si el archivo está vacío, escribe el encabezado
            if file.tell() == 0:
                writer.writeheader()
    # Escribir los resultado_voting del diccionario en el archivo CSV
            writer.writerow(resultado_voting)
        print(f"Se ha guardado el diccionario en el archivo CSV: {archivo_csv}")
        
        # resultado_db = db.Resultados(**resultado_voting)
        # db.session.add(resultado_db)
        # db.session.commit()

        requests.delete("http://localhost:5002/rating/"+str(resultados[0]['id']))
    else:
        print("No hay suficientes resultados para verificar.")
 
