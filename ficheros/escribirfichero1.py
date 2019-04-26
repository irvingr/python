# Grabar en un fichero de texto con Python

fichero = open("fichero_para_escribir.txt", "wt", encoding="UTF-8")

texto_del_fichero = "Hola, esta es la línea que vamos a escribir en el fichero de texto."

fichero.write(texto_del_fichero)

fichero.close()