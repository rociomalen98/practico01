"""Decorador Simple para Mostrar Mensajes: Crear un decorador con el nombre 
“decorador_mensaje” que imprima un mensaje antes y después de la ejecución 
de la función decorada.
Crear una función con el nombre “funcion_principal” queimprima en pantalla el
texto: “Esta es la función principal”.
Decorar esta funcion con el decorador y luego ejecutarla"""
def decorador_mensaje(func):
    def wrapper():
        print("Inicio de la función.")
        func()  
        print("Fin de la función.")
    return wrapper


@decorador_mensaje
def funcion_principal():
    print("Esta es la función principal.")

# Probamos la función decorada
funcion_principal()
