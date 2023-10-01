import csv
import requests

archivo_csv = "autenticacion.csv"
# Abrir el archivo CSV en modo de escritura
with open(archivo_csv, mode="a", newline="") as file:
    # Crear un objeto escritor CSV
    writer = csv.DictWriter(file, fieldnames=["id", "Rol", "Token", "Respuesta_esperada", "Respuesta_obtenida", "revision"])
    
    for i in range(0, 100):
        r = requests.post("http://localhost:5000/user")

        print(r.json()['rol'])

        headers = {'Content-Type': 'application/json',
                'Authorization': "Bearer {}".format(r.json()['token'])}
        resultados = requests.get(
            "http://127.0.0.1:5000/ver-resultados", headers=headers)
        
        if r.json()['rol']=="admin":
            respuesta_esp = "Acceso permitido"
        else:
            respuesta_esp = "No autorizado"

        data = {
            "id": i + 1,
            "Rol": r.json()['rol'],
            "Token": r.json()['token'],
            "Respuesta_esperada": respuesta_esp,
            "Respuesta_obtenida": resultados.text,
            "revision": respuesta_esp == resultados.text
        }
        
        # Si el archivo está vacío, escribe el encabezado
        if file.tell() == 0:
            writer.writeheader()
        # Escribir los resultados del diccionario en el archivo CSV
        writer.writerow(data)
        print(f"Se ha guardado el diccionario en el archivo CSV: {archivo_csv}")




