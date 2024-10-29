"""Crear un script con una lista mi_lista que contenga tres tipos diferentes de datos.
Agregar un nuevo elemento al final de la lista con el método append().
Cambiar el valor del primer elemento de la lista.
Eliminar el último elemento de la lista con el método pop().
Mostrar en pantalla el contenido de la lista."""

# Creación de una lista con diferentes tipos de datos
mi_lista = [26, "Rocio", 1.58]
mi_lista.append("basquet")

#cambiar el valor del primer elemento de la lista
mi_lista[0] = "27"

#eliminar ultimo elemento de la lista
mi_lista.pop(3)

#mostrar el contenido de la lista
print(mi_lista)
