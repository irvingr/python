# Diccionarios - Colección de elementos que están indexados, no están ordenados y se pueden modificar.
# Son escritos entre {} y están formados por pares de elementos clave:valor

diccionario_colores = {"red":"rojo", "blue":"azul", "yellow":"amarillo"}
print(diccionario_colores) # {"red":"rojo", "blue":"azul", "yellow":"amarillo"}

# Acceder a elementos de un diccionario:
print(diccionario_colores["red"]) # rojo

valor1 = diccionario_colores["yellow"]
print(valor1) # yellow

# Agregar elementos a un diccionario:
diccionario_colores["black"] = "negro"
print(diccionario_colores) # {"red":"rojo", "blue":"azul", "yellow":"amarillo", "black":"negro"}

# Eliminar elementos de un diccionario:
print(diccionario_colores.pop("yellow")) # amarillo - Devuelve el elemento eliminado.

print(diccionario_colores) # {'red': 'rojo', 'blue': 'azul', 'black': 'negro'}

del(diccionario_colores["black"])
print(diccionario_colores) # {'red': 'rojo', 'blue': 'azul'}

# Recorrer un diccionario
for color in diccionario_colores :
    print(color) # Imprime las claves de los elementos del diccionario.

for clave, valor in diccionario_colores.items() :
    print(f'{clave} : {valor}') # Imprime las claves y valores de los elementos del dicionario.