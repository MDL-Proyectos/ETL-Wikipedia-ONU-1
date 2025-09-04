import json
from dotenv import load_dotenv
import os

load_dotenv()

# Cargar y leer el archivo generado a través del proyecto WebScraping--1
with open(os.getenv("DATA_JSON_PATH"), 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Obtenemos las claves del primer diccionario en la lista
print(datos[0].keys())


#print(datos[0]["Denominación UNTERM[23]\u200b[i]\u200b"])

for dato in datos:
    print(dato["Estado miembro[13]\u200b"])  # País
    print(dato["Denominación UNTERM[23]\u200b[i]\u200b"])  # Denominación
    print(dato["Fecha de admisión[13]\u200b"])  # Fecha de admisión
    print(dato["Notas"])  # Notas
    print("-----")