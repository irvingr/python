# Operadores de identidad (is, is not)
# - - > Identifica si dos objetos son iguales o diferentes

paises1 = ['México', 'Francia']
paises2 = ['México', 'Francia']
paises3 = paises1

print(paises3 is paises1) # True

paises3.append('Japon') # Agregar un elemento a una lista.

print(paises3) # ['México', 'Francia', 'Japon']
print(paises1) # ['México', 'Francia', 'Japon']
print(paises2) # ['México', 'Francia']

print(paises3 is not paises1) # False