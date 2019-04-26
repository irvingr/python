# Leer un fichero de texto en Python

fichero = open('fichero_para_leer.txt', 'rt', encoding="utf-8") # Abrir archivo en modo lectura y de tipo texto con códificación UTF-8.
datos_fichero = fichero.read() # Leer el fichero.
print(datos_fichero) # Mostrar datos del fichero.