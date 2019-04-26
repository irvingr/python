# Bucle for

# Iterar sobre una lista.
print("- - - - - - - - - - Lista - - - - - - - - - -")
marcas = ["hp", "lenovo", "gateway", "toshiba"]
for marca in marcas:
    print(marca)

# Iterar sobre un string.
print("- - - - - - - - - - String - - - - - - - - - -")
cadena = "Python"
for caracter in cadena:
    print(caracter)

# Iterar sobre un rango.
print("- - - - - - - - - - Rango - - - - - - - - - -")
print("=> De 0 al 7")
for numero in range(8):
    print(numero)

print("=> De 3 al 7")
for numero in range(3,8):
    print(numero)

print("=> De 0 al 7 de dos en dos")
for numero in range(3,8,2):
    print(numero)

# break - parar el bucle
print("=> Break")
for numero in range(10):
    if (numero == 5):
        break
    print(numero)

# continue - para sólo la iteracción actual
print("=> Continue")
for numero in range(10):
    if (numero == 6):
        continue
    print(numero)

# for doble
print("=> for doble")
for numero1 in range(4):
    for numero2 in range(3):
        print(numero1, numero2)