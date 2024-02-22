import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(ruta_archivo):
    # Cargar datos desde un archivo CSV
    datos = pd.read_csv(ruta_archivo, skiprows=5)
    return datos

def limpiar_datos(datos):
    # Eliminar columnas según su nombre
    datos = datos.drop(['Temperatura del Aire % de datos ', 'Humedad Relativa % de datos '], axis=1)
    # Eliminar filas que contienen al menos un valor NaN
    datos_limpios = datos.dropna()
    return datos_limpios

def limpiar_fechas(datos):
    # Eliminar las filas con texto no válido en la columna 'Tiempo UTC-4'
    datos = datos[datos['Tiempo UTC-4'].str.contains(r'^\d{2}-\d{2}-\d{4}$', regex=True, na=False)]
    # Convertir la columna 'Tiempo UTC-4' a tipo de fecha
    datos['Tiempo UTC-4'] = pd.to_datetime(datos['Tiempo UTC-4'], format='%d-%m-%Y')
    return datos

def calcular_temperatura_promedio_por_mes(datos):
    # Calcular el promedio de temperatura por mes
    datos['Mes'] = datos['Tiempo UTC-4'].dt.month
    temperatura_promedio_mes = datos.groupby('Mes')['Temperatura del Aire ºC'].mean()
    # Alinear los índices con el rango esperado de 1 a 12
    temperatura_promedio_mes = temperatura_promedio_mes.reindex(range(1, 13))
    return temperatura_promedio_mes

def graficar_temperatura_promedio_por_mes(temperatura_promedio_mes):
    # Graficar la temperatura promedio por mes
    plt.figure(figsize=(10, 6))
    plt.bar(temperatura_promedio_mes.index, temperatura_promedio_mes.values, color='skyblue')
    plt.title('Temperatura Promedio por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Temperatura del Aire ºC')
    plt.xticks(temperatura_promedio_mes.index, ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'], rotation=45)
    plt.show()

def calcular_humedad_promedio_por_mes(datos):
    # Calcular el promedio de humedad relativa por mes
    humedad_promedio_mes = datos.groupby('Mes')['Humedad Relativa %'].mean()
    return humedad_promedio_mes

def graficar_humedad_promedio_por_mes(humedad_promedio_mes):
    # Graficar la humedad relativa promedio por mes
    plt.figure(figsize=(10, 6))
    plt.bar(humedad_promedio_mes.index, humedad_promedio_mes.values, color='lightgreen')
    plt.title('Humedad Relativa Promedio por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Humedad Relativa %')
    plt.xticks(humedad_promedio_mes.index, ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'], rotation=45)
    plt.show()

def calcular_correlacion(datos):
    # Calcular la correlación entre temperatura y humedad
    correlacion = datos['Temperatura del Aire ºC'].corr(datos['Humedad Relativa %'])
    print(f"Correlación entre Temperatura y Humedad: {correlacion}")

if __name__ == "__main__":
    # Cargar datos
    datos = cargar_datos('C:/Users/jose_/OneDrive/Escritorio/Clima_Arica/agrometeorologia-20240222121632.csv')
    # Limpiar datos
    datos_limpios = limpiar_datos(datos)
    # Limpiar fechas
    datos_limpios = limpiar_fechas(datos_limpios)
    # Calcular temperatura promedio por mes
    temperatura_promedio_mes = calcular_temperatura_promedio_por_mes(datos_limpios)
    # Graficar temperatura promedio por mes
    graficar_temperatura_promedio_por_mes(temperatura_promedio_mes)
    # Calcular humedad promedio por mes
    humedad_promedio_mes = calcular_humedad_promedio_por_mes(datos_limpios)
    # Graficar humedad promedio por mes
    graficar_humedad_promedio_por_mes(humedad_promedio_mes)
    # Calcular correlación
    calcular_correlacion(datos_limpios)
