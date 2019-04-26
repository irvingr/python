# SQLite - Insertar varios registros a la base de datos

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

lista_personas = [ ('Karl', 'Gonzalez', 'Range', 33), ('George', 'Rachell', 'Forten', 35), ('Mary', 'Jan', 'Luke', 29) ]

cursor.executemany("INSERT INTO PERSONAS (nombre, apellido1, apellido2, edad) VALUES (?, ?, ?, ?)", lista_personas)

conexion.commit()

conexion.close()