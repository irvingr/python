# incluir datos a un fichero de texto.

fichero = open("fichero_para_leer.txt", "at", encoding="UTF-8")

cadena_para_incluir = "\nEstá es la tercera fila del fichero"

fichero.write(cadena_para_incluir)

fichero.close()