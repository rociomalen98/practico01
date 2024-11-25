"""Crear un script de python que contenga una función con el
nombre “sumar_lista”, reciba como único parámetros una lista de
números y retorne la sumatoria de todos los números de la lista"""

def sumar_lista(numeros):
    return sum(numeros)

# Prueba la función
print("la suma de la lista es:", sumar_lista([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Salida: 36
print("la suma de la lista es:", sumar_lista([5, 9]))  # Salida: 14
