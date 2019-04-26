# SQLite3 - Consultar datos y ordenarlos por alguna columna

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")

lista_personas_ordenada = cursor.fetchall()

for persona in lista_personas_ordenada:
    print(persona)

conexion.close()

# (4, 'Mary', 'Jan', 'Luke', 29)
# (2, 'Karl', 'Gonzalez', 'Range', 33)
# (3, 'George', 'Rachell', 'Forten', 35)
# (1, 'Joseph', 'Mark', 'Lee', 45)