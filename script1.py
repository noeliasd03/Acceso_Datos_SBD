import requests
import pymongo
import time
from datetime import datetime

# configuracion mongo
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
db = cliente["citybikes"]
coleccion = db["estaciones"]

# URL de la API
url = "http://api.citybik.es/v2/networks"

intervalo = 120  # 2 minutos

while True:
    try:
        # datos de la API
        respuesta = requests.get(url)
        datos = respuesta.json()

        # guardar en mongo
        timestamp = datetime.now()
        for network in datos["networks"]:
            network["timestamp"] = timestamp
            coleccion.insert_one(network)

        print(f"Datos insertados con éxito a las {timestamp}")
        
    except Exception as e:
        print(f"Error: {e}")

    # esperar el intervalo
    time.sleep(intervalo)

