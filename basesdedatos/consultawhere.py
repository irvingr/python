# SQLite3 - Consultar datos que cumplan con una determinada condición

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS WHERE edad >= 30 AND edad < 40")

personas_seleccionadas = cursor.fetchall()

for persona in personas_seleccionadas:
    print(persona)

conexion.close()

# (2, 'Karl', 'Gonzalez', 'Range', 33)
# (3, 'George', 'Rachell', 'Forten', 35)