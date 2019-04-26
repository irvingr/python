# tkinter - Componente label

import tkinter

raiz = tkinter.Tk()
raiz.title("Componente label")
# Creamos el componente label(etiqueta)

texto = "Hello World"
etiqueta = tkinter.Label(raiz, text=texto)
etiqueta.config(fg="green", bg="lightgrey", font=("Cortana",30))
etiqueta.pack()

raiz.mainloop()