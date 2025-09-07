# ETL-Wikipedia-ONU-1
Normalización y almacenamiento de datos provenientes del proyecto de web scraping.
# Proyecto ETL: Estados Miembros de la ONU

Este repositorio corresponde a la **segunda etapa** del proyecto sobre los Estados miembros de la ONU. Aquí se realiza el proceso de **ETL (Extract, Transform, Load)**, tomando como fuente los datos extraídos mediante web scraping en la primera parte del proyecto ([ver repositorio WebScraping--0](https://github.com/MDL-Proyectos/WebScraping-proyecto-1.git)).

## 🌐 Objetivo

Procesar, limpiar y almacenar en una base de datos PostgreSQL la información estructurada sobre los países miembros de la ONU, previamente obtenida desde Wikipedia. El objetivo final es contar con datos normalizados y listos para análisis y visualización.

## 🛠️ Tecnologías utilizadas

- Python 3
- psycopg2 (conexión a PostgreSQL)
- python-dotenv (manejo de variables de entorno)
- pandas (opcional para análisis)
- PostgreSQL

## 📦 Instalación

1. Clona el repositorio.
2. Instala las dependencias necesarias:

```bash
pip install psycopg2-binary python-dotenv pandas
```

3. Configura el archivo `.env` con tus credenciales de base de datos y la ruta al archivo JSON generado en la etapa de scraping:

```env
DB_HOST=
DB_DATABASE=
DB_PORT=
DB_USER= tu_usuario
DB_PSS= tu_contraseña

DATA_JSON_PATH= \paises-2.json
```

## ▶️ Ejecución

Ejecuta el script principal para iniciar el proceso ETL:

```bash
python main.py
```

El script realiza las siguientes etapas:
1. **Extract:** Lee el archivo JSON generado en la etapa de scraping.
2. **Transform:** Limpia y normaliza los datos (corrige nombres, fechas, elimina caracteres extra, etc.).
3. **Load:** Inserta los datos en la base de datos PostgreSQL en la tabla `paises_onu`.

## ⚙️ Estructura del repositorio

```
├── main.py                  # Script principal del proceso ETL
├── extract_data.py          # Módulo de extracción de datos
├── transform_data.py        # Módulo de transformación y normalización
├── connection_db.py         # Módulo de conexión y carga en PostgreSQL
├── .env                     # Variables de entorno (no subir credenciales reales)
├── README.md                # Documentación del proyecto
```

## 🔗 Relación con la primera etapa

Este proyecto depende del archivo JSON generado en el repositorio [WebScraping--0](../WebScraping--0), donde se realiza el scraping de Wikipedia para obtener los datos originales de los países miembros de la ONU.

## ⚖️ Consideraciones éticas

- Los datos procesados provienen de contenido público de Wikipedia.
- Se respeta la privacidad y las buenas prácticas de manejo de datos.

## ✍️ Autor

Matias DL

---
