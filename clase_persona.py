"""Crear una clase llamada `Persona` que tenga los atributos `nombre` y `edad`.
Además, debe tener un método `saludar` que imprima un saludo incluyendo el nombre
de la persona."""
class Persona:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def saludar(self):
    print(f"Hola, mi nombre es {self.name} y tengo {self.age} años.")

persona1 = Persona("Juan", 25)
persona1.saludar() 