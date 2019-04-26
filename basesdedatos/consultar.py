# SQLite3 - Consultar datos de una tabla

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS")

personas = cursor.fetchall()

for persona in personas:
    print(persona)

conexion.close()

# (1, 'Joseph', 'Mark', 'Lee', 45)
# (2, 'Karl', 'Gonzalez', 'Range', 33)
# (3, 'George', 'Rachell', 'Forten', 35)
# (4, 'Mary', 'Jan', 'Luke', 29)
