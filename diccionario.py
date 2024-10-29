"""Crear un script con un diccionario mi_diccionario con tres pares declave:valor,
de 3 tipos diferentes
Imprimir el valor de la primer clave.
Añade un nuevo par clave:valor al diccionario.
Intenta cambiar el valor de la segunda clave existente.
Imprimir el contenido del diccionario en pantalla."""

mi_diccionario = {
    "nombre" : "rocio",
    "edad" : 27,
    "medida" : 1.58
}
#imprimir el valor de la primera clave
print("la primera clave es:", mi_diccionario["nombre"])

#añadir nueva clave:valor al diccionario
mi_diccionario["profesión"] = "Estudiante"
#intentar cambiar la segunda clave existente
mi_diccionario["edad"] = 26
#mostrar mi_diccionario
print("el diccionario creado es:", mi_diccionario)
