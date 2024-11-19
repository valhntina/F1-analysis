import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Definir la ruta para las visualizaciones
visualization_dir = "../visualizations"

# Equipos actuales de F1
equipos_actuales = [
    'Red Bull', 'Mercedes', 'Ferrari', 'McLaren', 'Alpine F1 Team',
    'Aston Martin', 'Haas F1 Team','Sauber', 'Williams', 'AlphaTauri'
]

# Función para cargar los datos
def cargar_datos():
    return pd.read_csv('../data/pilotos.csv')

# Función para analizar el rendimiento promedio de pilotos
def analizar_rendimiento_promedio_pilotos(df):
    # Seleccionar los pilotos
    pilotos_seleccionados = ['Max Verstappen', 'Lewis Hamilton', 'Charles Leclerc', 'Lando Norris']
    
    # Filtramos los datos solo para estos pilotos
    df_pilotos_seleccionados = df[df['Piloto'].isin(pilotos_seleccionados)]
    
    # Calculamos la posición promedio de los pilotos a lo largo de las temporadas
    df_rendimiento_piloto = df_pilotos_seleccionados.groupby(['Piloto', 'Año'])['Posición'].mean().reset_index()

    # Calculamos la posición promedio por piloto
    df_promedio_piloto = df_rendimiento_piloto.groupby('Piloto')['Posición'].mean().reset_index()

    # Verificamos los primeros datos
    print(df_promedio_piloto)

    # Escalar las posiciones promedio
    scaler = StandardScaler()
    df_promedio_piloto['Posición_scaled'] = scaler.fit_transform(df_promedio_piloto[['Posición']])

    # Aplicamos KMeans para agrupar los pilotos y se arregla el numero de clusters
    kmeans = KMeans(n_clusters=4, random_state=42)  # 4 clusters, uno por piloto
    df_promedio_piloto['Cluster'] = kmeans.fit_predict(df_promedio_piloto[['Posición_scaled']])

    # Visualizamos los resultados en un gráfico de dispersión
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df_promedio_piloto, x='Piloto', y='Posición', hue='Cluster', palette='viridis', s=100, marker='o')
    plt.title('Agrupamiento de los Tres Pilotos por Rendimiento Promedio')
    plt.xlabel('Piloto')
    plt.ylabel('Posición Promedio')
    plt.tight_layout()
    plt.savefig(f"{visualization_dir}/rendimiento_promedio_pilotos_clusters.png")
    plt.show()

# Función principal para ejecutar el análisis y generar las visualizaciones
def main():
    # Cargar los datos
    df = cargar_datos()

    # Realizar el análisis de los tres pilotos seleccionados y graficar los resultados
    analizar_rendimiento_promedio_pilotos(df)

if __name__ == "__main__":
    main()
