import serial  # Importa la librería para comunicación serial
import statistics as st  # Importa la librería de estadísticas y la renombra como "st"
import time  # Importa la librería para manejar tiempos de espera

# Configuración del puerto serial (ajustar según el puerto usado en el sistema)
ser = serial.Serial("COM3", 9600)  
# Lista para almacenar las mediciones de distancia
distancia = []
num_readings = 4  # Número de lecturas a realizar

# Bucle para obtener mediciones
for _ in range(num_readings):
    #try:
    data = float(ser.readline().decode().strip())  # Lee una línea del puerto serial, la decodifica y elimina espacios en blanco
    # Espera 3 segundos entre lecturas
    #if data:  
        #distancias = float(data)  # Convierte el dato recibido a tipo flotante
    distancia.append(data)  # Almacena la distancia en la lista
    print(f"Distancia medida: {data} cm")  # Muestra la distancia medida
    time.sleep(10)
    #except ValueError:
        #print("Error en la conversión de datos")  # Mensaje de error si la conversión falla

# Cierra la comunicación serial
ser.close()

# Si se obtuvieron datos, se calculan estadísticas
if distancia:
    #promedio = sum(distancia) / len(distancia)  # Calcula el promedio manualmente
    media = st.mean(distancia)  # Calcula la media (promedio)
    mediana = st.median(distancia)  # Calcula la mediana
    moda = st.mode(distancia) # Calcula la moda
    desviacion_estandar = st.stdev(distancia)  # Calcula la desviación estándar

    # Muestra los resultados estadísticos
    print("\nResultados estadísticos:")
    print(f"Media: {media:.2f} cm")
    print(f"Mediana: {mediana:.2f} cm")
    print(f"Moda: {moda:.2f} cm")
    print(f"Desviación estándar: {desviacion_estandar:.2f} cm")
else:
    print("No se pudieron obtener datos del sensor.")  # Mensaje si no se obtuvieron datos