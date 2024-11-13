import numpy as np

def calcular_volumen(x_min, x_max, y_min, y_max, n, m, funcion_z):
    #Aquí se define el tamaño en cada eje, basado en el número de divisiones n
    dx = (x_max - x_min) / n
    dy = (y_max - y_min) / m

    #Se inicializa el volumen
    volumen = 0

    #Iterar sobre cada sección de los ejes x, y
    for i in range(n):
        for j in range(m):
            # Coordenadas centrales de cada cuboide pequeño
            x = x_min + (i + 0.5) * dx
            y = y_min + (j + 0.5) * dy

            z = funcion_z(x, y)

            volumen += dx * dy * z

            # Se obtiene dx y dy de acuerdo a la fórmula

    return volumen

# Aquí va la función
def funcion_z(x, y):
    return x**2 + y**2

# Ejemplo de uso

n = int(input("Ingrese el número máximo de divisiones (n): "))
m = int(input("Ingrese el número máximo de divisiones (m): "))
a = int(input("Ingrese el valor mínimo en x: "))
b = int(input("Ingrese el valor máximo en x: "))
c = int(input("Ingrese el valor mínimo en y: "))
d = int(input("Ingrese el valor máximo en y: "))

x_min, x_max = a, b #límites en el eje x
y_min, y_max = c, d #límites en el eje y

volumen = calcular_volumen(x_min, x_max, y_min, y_max, n, m, funcion_z)
print(f"Volumen aproximado del objeto: {volumen}")
