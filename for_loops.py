"""a. Escribir un programa que muestre los números del 1 al 10
utilizando un bucle for.
b. Escribir un programa que muestre la suma de los números del
1 al 100."""

#la funcion in range() devuelve una secuencia de numeros no se si era lo que
# pedia el ejercicio pero lo vi en la documentacion de python y me parecio optimo usarlo
for x in range(10):
  print(x+1)

#punto B
suma = 0

for numero in range(1, 101):
    suma += numero

print("La suma de los números del 1 al 100 es:", suma)
