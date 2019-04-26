# SQLite3 - Actualizar datos de una tabla

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS SET edad = 40 WHERE nombre = 'Joseph'")

conexion.commit()

conexion.close()
