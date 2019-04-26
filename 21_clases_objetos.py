# Clases y objetos. Programación orientada a objetos POO

# Clase
class ClaseSilla:
    color = "blanco"
    precio = 100

objetoSilla1 = ClaseSilla()

print(objetoSilla1.color) # blanco
print(objetoSilla1.precio) # 100

objetoSilla2 = ClaseSilla()

objetoSilla2.color = "verde"
objetoSilla2.precio = 120

print(objetoSilla2.color) # verde
print(objetoSilla2.precio) # 120

class Persona:
    # Método constructor  
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # Método saludar
    def saludar(self):
        print("Hola, me llamo {} y tengo {} años".format(self.nombre, self.edad))

# Invocar a la clase Persona.
persona1 = Persona("Maria", 27)

print(persona1.nombre) # Maria
print(persona1.edad) # 27

# Invocar al método saludar de la clase Persona.
persona1.saludar() # Hola, me llamo Maria y tengo 27 años