import requests
import pandas as pd

# Lista de años a analizar
anios = range(2014, 2024)

# Función para obtener los datos de la API con paginación
def obtener_datos_f1(anio):
    offset = 0
    datos = []
    while True:
        url = f"https://ergast.com/api/f1/{anio}/results.json?limit=100&offset={offset}"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos_pagina = respuesta.json()
            # Si no hay más resultados, rompemos el bucle
            if not datos_pagina['MRData']['RaceTable']['Races']:
                break
            datos.extend(datos_pagina['MRData']['RaceTable']['Races'])
            offset += 100 
        else:
            print(f"Error al obtener datos para {anio}")
            break
    return datos

# Lista para almacenar todos los registros
datos_totales = []

# Recopilación de datos de cada año
for anio in anios:
    print(f"Obteniendo datos para {anio}...")
    carreras = obtener_datos_f1(anio)
    if carreras:
        for carrera in carreras:
            circuito = carrera['Circuit']
            for resultado in carrera['Results']:
                fila = {
                    'Año': anio,
                    'Carrera': carrera['raceName'],
                    'Fecha': carrera['date'],
                    'Circuito': circuito['circuitName'],
                    'Localización': f"{circuito['Location']['locality']}, {circuito['Location']['country']}",
                    'Piloto': f"{resultado['Driver']['givenName']} {resultado['Driver']['familyName']}",
                    'Equipo': resultado['Constructor']['name'],
                    'Posición': resultado['position'],
                    'Vueltas Completadas': resultado['laps'],
                    'Tiempo': resultado['Time']['time'] if 'Time' in resultado else None,
                }
                datos_totales.append(fila)

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(datos_totales)

# Guardar los datos en un archivo CSV
df.to_csv('../data/pilotos.csv', index=False)
print(f"Se han guardado {len(df)} registros en pilotos.csv.")
