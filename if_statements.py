"""Escribir un script que le asigne a una variable un número y muestre si es 
positivo, negativo o cero. Utilizando unicamente la sentencia IF"""

numero = float(input("Por favor, ingresa un número: "))

#verificar si el numero es positivo, negativo o cero solo con if
if numero > 0:
    print("El número ingresado es positivo.")

if numero < 0:
    print("El número ingresado es negativo.")

if numero == 0:
    print("El número ingresado es cero.")
