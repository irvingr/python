# SQLite 3 - Crear tabla

import sqlite3

conexion = sqlite3.connect("basededatos1.db") # Abrir conexion

cursor = conexion.cursor() # Objeto cursor utilizado para ejecutar sentencias SQL.

cursor.execute("CREATE TABLE PERSONAS (id_persona INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")

conexion.commit()

conexion.close()
