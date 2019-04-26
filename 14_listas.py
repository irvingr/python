# Listas - Colección de elementos que está ordenada y se puede modificar. Se definen con []

colores = ['azul', 'rojo', 'amarillo']

print(colores) # ['azul', 'rojo', 'amarillo']
print(colores[1]) # rojo
print(colores[2]) # amarillo

colores[2] = "verde"
print(colores[2]) # verde

print(colores) # ['azul', 'rojo', 'verde']


# Longitud de una lista:
print(len(colores)) # 3


# Agregar elementos a una lista:
colores.append('blanco')
print(colores) # ['azul', 'rojo', 'verde', 'blanco']
print(colores[3]) # blanco


# Eliminar elementos de una lista:
colores.remove('azul')
print(colores) # [rojo', 'verde', 'blanco']


# Recorrer una lista:
for color in colores :
    print(color)


# Ordenar listas
colores.sort()
print(colores) # ['blanco', 'rojo', 'verde']


# Limpiar una lista:
colores.clear()
print(colores) # []