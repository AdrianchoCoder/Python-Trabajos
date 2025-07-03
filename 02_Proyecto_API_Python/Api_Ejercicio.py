import requests
import json

#Link de La API a sacar la Informacion
url = "https://api-colombia.com/api/v1/Department"
try:
    respuesta = requests.get(url, timeout=10)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        for atraccion in datos:
            id = atraccion.get("id", "Id No Disponible")
            nombre = atraccion.get("name", "Nombre No Disponible")
            poblacion = atraccion.get("population", "Poblacion No Disponible")
            descripcion = atraccion.get("description", "Descripcion No Disponible")
            print("Id:", id)
            print("Nombre: ", nombre)
            print("Poblacion: ", poblacion)
            print("Descripcion: ", descripcion)
    else:
        print(f"Error en la solicitud: Codigo{respuesta.status_code}")

except requests.exceptions.RequestException as error:
    print(f"Error de Conexion: {error}")
