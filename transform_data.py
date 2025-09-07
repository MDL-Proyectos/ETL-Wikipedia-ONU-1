import re

class DataTransformer:
    def __init__(self):
        
        pass

    @staticmethod    
    def normalize_data(nombre):
        if not isinstance(nombre, str):
            # El método isinstance(obj, tipo) verifica si el objeto obj es del tipo especificado.
            nombre = ""
        string_normalizado = re.sub(r'\[.*?\]|[\u200b]', '', nombre).strip()
        return string_normalizado
    
    @staticmethod
    def normalize_date(fecha_str):
        MESES = {
            "enero": "01",
            "febrero": "02",
            "marzo": "03",
            "abril": "04",
            "mayo": "05",
            "junio": "06",
            "julio": "07",
            "agosto": "08",
            "septiembre": "09",
            "octubre": "10",
            "noviembre": "11",
            "diciembre": "12"
        }
        # el formato que viene de la página es: "25 de agosto de 1980"
        partes = fecha_str.split(" de ") # Divide la cadena en partes usando " de " como separador
        if len(partes) == 3:
            dia, mes, anio = partes
            mes_num = MESES.get(mes.lower())
            if mes_num:
                return f"{anio}-{mes_num}-{dia.zfill(2)}"
        return None

