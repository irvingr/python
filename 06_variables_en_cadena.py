# Imprimir variables en una cadena

nombre = 'Irving'
edad = 25
print('Buenos días ' + nombre)
print("Buenos días " + nombre)
print("Buenos días",nombre)

# .format
print("Buenos días {}, feliz cumpleaños #{}".format(nombre, edad))

resultado = 45 / 7

print('El resultado es {r}'.format(r=resultado))
print('El resultado es {r:1.3f}'.format(r=resultado))

# f-strings <= apartir de python 3.6
pais ='México'
print(f"{nombre}, bienvenido a {pais}")