# Funciones de cadena

cadena = "Esto es una cadena de texto"
cadena2 = "grape,apple,orange,banana"

length = len(cadena) # Longitud de una cadena.
upper = cadena.upper() # Convierte string en mayúsculas.
lower = cadena.lower() # Convierte string en minúsculas.

# Separar string

split = cadena.split()
split2 = cadena2.split(',')

print(cadena)
print('Longitud de la cadena =>',length)
print('String en mayúsculas =>',upper)
print('String en minúsculas =>',lower)
print('Separar string =>',split)
print('String separado por , =>',split)
