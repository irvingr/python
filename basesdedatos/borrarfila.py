# SQLite3 - Borrar datos de una tabla

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'George'")

conexion.commit()

conexion.close()