import json
from dotenv import load_dotenv
import os

def extract():

    load_dotenv()

    # Cargar y leer el archivo generado a través del proyecto WebScraping--1
    with open(os.getenv("DATA_JSON_PATH"), 'r', encoding='utf-8') as f:
        datos = json.load(f)

    # Obtenemos las claves del primer diccionario en la lista
   # print(datos[0].keys())


    #print(datos[0]["Denominación UNTERM[23]\u200b[i]\u200b"])

    for dato in datos:
        # Con el método pop() corregimos el nombre de la clave. Normalizamos el nombre de la clave.
        dato["Estado miembro"] = dato.pop("Estado miembro[13]\u200b")
        dato["Denominación UNTERM"] = dato.pop("Denominación UNTERM[23]\u200b[i]\u200b")
        dato["Fecha de admisión"] = dato.pop("Fecha de admisión[13]\u200b")
        #print(dato["Fecha de admisión"])


        
    return datos