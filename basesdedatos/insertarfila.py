# SQLite 3 - Insertar datos en una tabla

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS (nombre, apellido1, apellido2, edad) VALUES('Joseph', 'Mark', 'Lee', 45)")

conexion.commit()

conexion.close()