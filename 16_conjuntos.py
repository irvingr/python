# Conjuntos - Colección de elementos que esta desordenado, no hay un indice para poder acceder a sus elementos. Se definen con {}

conjunto_colores = {'verde', 'blanco', 'rojo'}
print(conjunto_colores) # {'blanco', 'verde', 'rojo'} ó {'rojo', 'verde', 'blanco'} ó {'rojo', 'blanco', 'verde'} ó {'verde', 'blanco', 'rojo'}

# Recorrer un conjunto:
for color in conjunto_colores :
    print(color)

# Longitud de un conjunto:
print(len(conjunto_colores)) # 3

# Agregar elemento a un conjunto:
conjunto_colores.add('café')
print(conjunto_colores)

# Eliminar elemento de un conjunto:
conjunto_colores.remove('verde')
print(conjunto_colores)