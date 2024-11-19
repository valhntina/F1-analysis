# Análisis y Visualización de Datos de la Fórmula 1

Este proyecto para DATA MINING realiza un análisis de los resultados de la Fórmula 1, con el objetivo de generar visualizaciones del rendimiento de los pilotos, equipos dominantes en cada temporada y la evolución del rendimiento de pilotos específicos. Las visualizaciones se generan utilizando bibliotecas como **Seaborn**, **Matplotlib** y **Pandas**.

## Funcionalidades

1. **Análisis del rendimiento por circuito**: Se generan gráficos de barras para mostrar el rendimiento promedio de los pilotos en cada circuito.
2. **Análisis de los equipos dominantes por temporada**: Muestra qué equipos han dominado cada temporada según el número de posiciones y victorias.
3. **Evolución del rendimiento de pilotos específicos**: Gráficos de línea para visualizar cómo ha evolucionado el rendimiento de pilotos a lo largo de las temporadas.
4. **Agrupamiento de pilotos según rendimiento promedio**: Utiliza **KMeans** para agrupar pilotos en clusters basados en su rendimiento promedio.

## Orden de ejecución:
1. fetch_data.py
2. cargar_datos.py
3. clustering.py


## Requisitos
- **Python 3.x**
- **Bibliotecas**:
  - pandas
  - seaborn
  - matplotlib
  - scikit-learn
  - requests
