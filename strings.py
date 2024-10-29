"""Crear un script de python que contenga una variable mi_nombre y asignarle tu
nombre como string. Luego mostrar el tipo de datos de la variable.
Intentar acceder a la primera y última letra de mi_nombre utilizando índices y
mostrándolos en pantalla.
Utilizar la función len() para calcular la longitud de mi_nombre y mostrarlo.
Imprimir en pantalla el contenido de la variable mi_nombre, todo en mayusculas y
todo en minúsculas."""

mi_nombre = "rocio"

#muestra tipo de dato de varible
print("Tipo de dato de la variable 'mi_nombre':",type(mi_nombre))

#muestra la primera y ultima letra
print("Primera letra del nombre:",mi_nombre[0], "ultima letra del nombre",mi_nombre[4])

#muestra la longitud del nombre
print("Longitud del nombre:",len(mi_nombre))

#muetra el nombre en mayuscula
print("Nombre en mayuscula:", mi_nombre.upper())

#nombre en minuscula
print("Nombre en minuscula:", mi_nombre.lower())
