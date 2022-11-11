import psycopg2
import json
# Leer las credenciales de un archivo JSON
with open("credenciales_ejemplo.json") as archivo_credenciales:
    credenciales = json.load(archivo_credenciales)
try:
    conexion = psycopg2.connect(**credenciales)
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)
