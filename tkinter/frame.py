# tkinter - Componente frame

import tkinter

raiz = tkinter.Tk()

raiz.title("Componente frame")

# Creamos el componente frame

frame = tkinter.Frame(raiz)
frame.config(bg="grey", width=400, height=300)
frame.pack()


raiz.mainloop()