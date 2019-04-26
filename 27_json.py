# JSON

# Convertir datos de un diccionario Python a una estructura JSON

producto1 = {"nombre" : "silla", "color" : "blanco", "precio" : 85}

import json

estructura_json = json.dumps(producto1)

print(estructura_json)


# Convertir una estructura JSON (estructura_json) en un diccionario en Python

producto2 = json.loads(estructura_json)

print(producto2)
print(producto2["precio"])
