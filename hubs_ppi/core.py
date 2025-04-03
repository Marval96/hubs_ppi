import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analizar_hubs(archivo_csv, percentil_usuario):
    """
    Carga un archivo CSV con métricas de centralidad de nodos, calcula los scores de importancia,
    genera un CSV con los resultados y crea un gráfico de la distribución de scores.
    
    Parámetros:
    - archivo_csv: str, nombre del archivo CSV de entrada.
    - percentil_usuario: float, percentil de nodos a destacar (ejemplo: 95 para el top 5%).

    Salida:
    - Guarda un archivo CSV con los scores de importancia.
    - Guarda un gráfico PNG con la distribución de los hubs.
    - Imprime los resultados en consola.
    """

    # Cargar el archivo CSV
    df = pd.read_csv(archivo_csv)

    # Definir métricas de centralidad
    metricas = ['MCC', 'DMNC', 'MNC', 'Degree', 'EPC', 'BottleNeck', 'EcCentricity',
                'Closeness', 'Radiality', 'Betweenness', 'Stress', 'ClusteringCoefficient']

    # Calcular Z-scores
    for metrica in metricas:
        if metrica in df.columns:  # Verificar que la métrica exista en el archivo
            df[f'z_{metrica}'] = (df[metrica] - df[metrica].mean()) / df[metrica].std()

    # Calcular el Score promedio
    z_columns = [f'z_{m}' for m in metricas if f'z_{m}' in df.columns]  # Solo incluir columnas generadas
    df['Score_promedio'] = df[z_columns].mean(axis=1)

    # Ordenar resultados
    resultado = df.sort_values(by='Score_promedio', ascending=False)

    # Guardar el archivo con los scores de todos los nodos
    nombre_salida = f"hubs_{archivo_csv.replace('.csv', '')}_scores.csv"
    resultado.to_csv(nombre_salida, index=True)
    print(f"\n Matriz de importancia generada y guardada como '{nombre_salida}'")

    # Seleccionar y mostrar hubs en el percentil definido por el usuario
    percentil = resultado['Score_promedio'].quantile(percentil_usuario / 100)
    hubs_destacados = resultado[resultado['Score_promedio'] >= percentil]

    print(f"\n Mostrando nodos en el top {100 - percentil_usuario}% de importancia:\n")
    print(hubs_destacados[['node_name', 'Score_promedio']])

    # Gráfico de la distribución de los hubs
    plt.figure(figsize=(8, 5))
    sns.histplot(resultado['Score_promedio'], kde=True, color='purple')
    plt.axvline(percentil, color='red', linestyle='--', label=f'Top {100 - percentil_usuario}%')
    plt.xlabel('Average Score (Z-score)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Importance Scores')
    plt.legend()
    
    # Guardar el gráfico en PNG con el mismo nombre que el CSV
    nombre_grafico = nombre_salida.replace('.csv', '.png')
    plt.savefig(nombre_grafico, dpi=1200, bbox_inches='tight')
    plt.show()

    print(f"\n Gráfico guardado como '{nombre_grafico}'")

    return resultado
