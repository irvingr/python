# Expresiones regulares ( search, findall, split, sub)

texto = "Hola, mi nombre es Irving"

# Importar módulo regular expressions
import re
# Invocar al método search - busca un patrón en una cadena

print(re.search("nombre", texto)) # <re.Match object; span=(9, 15), match='nombre'>
print(re.search("adios", texto)) # None

resultado = re.search("adios", texto)
if (resultado):
    print("Cadena encontrada")
else:
    print("Cadena No encontreada")

# Buscar coincidencias al final de una cadena - $

busca_final = re.search("Irving$", texto)
print(busca_final) # <re.Match object; span=(19, 25), match='Irving'>

# Buscar coincidencias al inicio de una cadena - ^

busca_inicio = re.search("^Hola", texto)
print(busca_inicio) # <re.Match object; span=(0, 4), match='Hola'>

# Buscar dos o más coincidencias - .*
buscar = re.search("mi.*es", texto)
print(buscar) # <re.Match object; span=(6, 18), match='mi nombre es'>

# findall - Busca todas las ocurrencias en una cadena.

texto2 = """
    El coche de Juan es rojo,
    el coche de José es blanco,
    y el coche de Georgina es rojo
"""

findall = re.findall("coche.*rojo", texto2)
print(findall)  # ['coche de Juan es rojo', 'coche de Georgina es rojo']

# split - Divide una cadena a partir de un patrón.

texto3 = "La silla es blanca y vale 80"
# Separar por espacios la cadena.
split = re.split(r"\s", texto3)
print(split) # ['La', 'silla', 'es', 'blanca', 'y', 'vale', '80']

# sub - substituye la palabra de una cadena.

sub = re.sub("blanca", "roja", texto3)
print(sub) # La silla es roja y vale 80