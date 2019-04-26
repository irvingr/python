# Escribir N cantidad de líneas en un fichero.
fichero = open("fichero_para_borrar.txt", "wt", encoding="UTF-8")

for line in range(1,26):
    fichero.write("Se escribio la línea: {l}\n".format(l=line))

fichero.close()