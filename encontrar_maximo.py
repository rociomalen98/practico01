"""Crear un script de Python que contenga una función con el nombre “encontrar_maximo”,
reciba como único parámetro una lista de números y retorne el número máximo
encontrado en la lista."""

def encontrar_maximo(numeros):
    return max(numeros)


# Prueba la función
print("El número máximo de la lista es: ", encontrar_maximo([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Salida: 9
print("El número máximo de la lista es: ", encontrar_maximo([2, 6, 5]))  # Salida: 6
