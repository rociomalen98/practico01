"""Escribir un programa que le solicite al usuario ingresar una calificación 
del 0 al 100, la asigne a una variable y muestre la calificación alfabética 
correspondiente (A, B, C, D, F) según el numero ingresado. Correspondiendo cada 
letra con valores de 20 en 20. Es decir: 0 a 19 = A, de 20 a 39 = B, etc"""

calificacion = float(input("Por favor, ingrese la calificacion, recordar que es del 1 al 100: "))

if 0 <= calificacion <= 19:
    print("La calificación alfabetica es: A")
elif 20 <= calificacion <= 39:
    print("La calificación alfabetica es: B")
elif 40 <= calificacion <= 59:
    print("La calificación alfabetica es: C")
elif 60 <= calificacion <= 79:
    print("La calificación alfabetica es: D")
elif 80 <= calificacion <= 100:
    print("La calificación alfabetica es: F")
else:
    print("Calificación fuera de rango permitido. Por favor, ingresa un número entre 0 y 100.")