import os
from dotenv import load_dotenv

from extract_data import extract
from transform_data import DataTransformer
from connection_db import PostgresDB

def main():
    load_dotenv()
    db = None
    try:
        db = PostgresDB()
        
        # 1. Extraer datos
        datos = extract()

        print("Datos extraídos:")
            #print(datos[0])  # Muestra el primer registro extraído para verificación
        print("Elementos: ", len(datos))  # Muestra la cantidad de registros extraídos
        
        # 2. Transformar datos
        for dato in datos:
            dato["Estado miembro"] = DataTransformer.normalize_data(dato.get("Estado miembro", ""))[:100]
            dato["Denominación UNTERM"] = DataTransformer.normalize_data(dato.get("Denominación UNTERM", ""))[:100]
            dato["Fecha de admisión"] = DataTransformer.normalize_data(dato.get("Fecha de admisión", ""))
            dato["Fecha de admisión"] = DataTransformer.normalize_date(dato.get("Fecha de admisión", ""))
            dato["Notas"] = DataTransformer.normalize_data(dato.get("Notas", ""))[:250]
            #print(dato["Estado miembro"])
        datos_transformados = datos
        
        print("Datos transformados:")
        # Muestra el primer registro transformado
        print(datos_transformados[0])  

        # 3. Cargar datos en la base de datos
        db.load_to_db(datos_transformados)
        print("Proceso ETL finalizado.")
    
    except Exception as e:
        print(f"Error durante el proceso ETL: {e}")
    
    finally:
       if db:
            db.close()
       

if __name__ == "__main__":
    main()