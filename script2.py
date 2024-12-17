import pandas as pd
import pymongo

# conectarse a mongo
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
bd = cliente["citybikes"]
coleccion = bd["estaciones"]

# datos de mongo
datos = list(coleccion.find({}, {
    "id": 1,
    "name": 1,
    "timestamp": 1,
    "free_bikes": 1,
    "empty_slots": 1,
    "uid": 1,
    "last_updated": 1,
    "slots": 1,
    "normal_bikes": 1,
    "ebikes": 1,
}))

# convertir id a texto (si no me falla al exportar a parquet)
for dato in datos: 
    dato["_id"] = str(dato["_id"])

# cargar datos en un dataframe de pandas
df = pd.DataFrame(datos)

# exportar a csv
df.to_csv("estaciones.csv", index=False)
print("Datos exportados a estaciones.csv")

# exportar a parquet
df.to_parquet("estaciones.parquet", index=False)
print("Datos exportados a estaciones.parquet")
