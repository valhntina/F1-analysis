import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


visualization_dir = "../visualizations"

# Equipos actuales de F1
equipos_actuales = [
    'Red Bull', 'Mercedes', 'Ferrari', 'McLaren', 'Alpine F1 Team',
    'Aston Martin', 'Haas F1 Team','Sauber', 'Williams', 'AlphaTauri'
]

# Función para cargar los datos
def cargar_datos():
    return pd.read_csv('../data/pilotos.csv')

# Función para agrupar pilotos menos destacados en "Otros"
def agrupar_pilotos(df):
    umbral = 5  # Número mínimo de apariciones para no ser agrupado
    pilotos_destacados = df['Piloto'].value_counts()[df['Piloto'].value_counts() >= umbral].index
    df.loc[:, 'Piloto'] = df['Piloto'].apply(lambda x: x if x in pilotos_destacados else 'Otros')
    return df

# Función para analizar el rendimiento de pilotos por tipo de circuito
def analizar_rendimiento_por_circuito(df):
    # Filtrar solo equipos actuales
    df = df[df['Equipo'].isin(equipos_actuales)]

    # Obtener tipos únicos de circuitos
    circuitos = df['Circuito'].unique()
    plt.figure(figsize=(15, len(circuitos) * 5))  # Tamaño ajustado para múltiples subgráficas

    for i, circuito in enumerate(circuitos):
        ax = plt.subplot(len(circuitos), 1, i + 1)

        # Filtrar datos del circuito actual
        df_circuito = df[df['Circuito'] == circuito]

        # Agrupar pilotos menos destacados en "Otros"
        top_pilotos = df_circuito['Piloto'].value_counts().head(15).index
        df_circuito.loc[~df_circuito['Piloto'].isin(top_pilotos), 'Piloto'] = 'Otros'

        # Crear gráfico de barras
        sns.barplot(data=df_circuito, x='Piloto', y='Posición', errorbar=None, ax=ax)
        ax.set_title(f'Rendimiento Promedio de los Pilotos en Circuitos {circuito}', fontsize=14)
        ax.set_xlabel('Piloto', fontsize=12)
        ax.set_ylabel('Posición Promedio', fontsize=12)
        ax.set_xticks(range(len(df_circuito['Piloto'].unique())))  # Define las posiciones de los ticks
        ax.set_xticklabels(df_circuito['Piloto'].unique(), rotation=45, ha='right', fontsize=10)  # Define las etiquetas

    # Ajustar diseño y guardar
    plt.tight_layout()
    plt.savefig(f"{visualization_dir}/rendimiento_por_circuito.png")
    plt.close()


# Función para analizar los equipos dominantes en cada temporada
def analizar_equipo_dominante(df):
    # Filtrar equipos actuales
    df = df[df['Equipo'].isin(equipos_actuales)]
    # Filtrar Posición 1, 2 y 3
    df_victorias = df[(df['Posición'] == 1) | (df['Posición'] == 2) | (df['Posición'] == 3)]

    equipos_dominantes = df_victorias.groupby(['Año', 'Equipo']).size().reset_index(name='Victorias')
    equipos_dominantes = equipos_dominantes.sort_values('Victorias', ascending=False).groupby('Año').head(1)


    plt.figure(figsize=(14, 8))
    sns.barplot(data=equipos_dominantes, x='Año', y='Victorias', hue='Equipo')

    plt.title('Equipos que Dominanaron en Cada Temporada')
    plt.xlabel('Temporada')
    plt.ylabel('Número de Victorias')
    plt.xticks(rotation=45)

    # Guardar la gráfica
    plt.tight_layout()
    plt.savefig(f"{visualization_dir}/equipos_dominantes_temporada.png")
    plt.close()


# Función para graficar la evolución del rendimiento de un piloto específico
def graficar_rendimiento_piloto(df, piloto):
    piloto_especifico = df[df['Piloto'] == piloto]

    plt.figure(figsize=(10, 6))
    plt.plot(piloto_especifico['Año'], piloto_especifico['Posición'], marker='o', color='b', label=piloto)

    plt.title(f'Evolución del Rendimiento de {piloto}')
    plt.xlabel('Año')
    plt.ylabel('Posición Promedio')
    plt.xticks(rotation=45)
    plt.legend()

    # Guardar la gráfica
    plt.tight_layout()
    plt.savefig(f"{visualization_dir}/rendimiento_{piloto}.png")
    plt.close()

# Función principal para ejecutar el análisis y guardar las visualizaciones
def main():
    # Cargar los datos
    df = cargar_datos()

    # Realizar los análisis y generar gráficos
    analizar_rendimiento_por_circuito(df)
    analizar_equipo_dominante(df)


    # Graficar el rendimiento de un piloto específico
    # Cambiar el nombre de acuerdo al piloto que se requiera la información
    piloto = 'Charles Leclerc' 
    graficar_rendimiento_piloto(df, piloto)

if __name__ == "__main__":
    main()