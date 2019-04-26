# pickle - Módulo para grabar ficheros binarios

import pickle

lista_colores = ['azul', 'rojo', 'verde', 'amarillo', 'negro']

fichero = open('fichero_colores.pckl', 'wb')

pickle.dump(lista_colores, fichero)

fichero.close()