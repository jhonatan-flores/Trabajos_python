from tkinter import *
etiqueta=Tk()
etiqueta.geometry("260x355")

invisible_uno=Label(etiqueta,text="")
invisible_uno.grid(row="0", column="1")

etiqueta_uno=Label(etiqueta,text="Nombre y Apellido")
etiqueta_uno.grid(row="1", column="1")

invisible_uno=Label(etiqueta,text="")
invisible_uno.grid(row="2", column="1")

etiqueta_dos=Label(etiqueta,text="DNI")
etiqueta_dos.grid(row="3", column="1")

invisible_uno=Label(etiqueta,text="")
invisible_uno.grid(row="4", column="1")

etiqueta_tres=Label(etiqueta,text="Celular")
etiqueta_tres.grid(row="5", column="1")

invisible_uno=Label(etiqueta,text="")
invisible_uno.grid(row="6", column="1")

cuadro_texto=Entry()
cuadro_texto.grid(row="1", column="2")

cuadro_texto=Entry()
cuadro_texto.grid(row="3", column="2")

cuadro_texto=Entry()
cuadro_texto.grid(row="5", column="2")

widget_uno=Frame()
widget_uno.grid(row="7", column="1", columnspan="2")
widget_uno.config(width=240 ,height=200)
widget_uno.config(bg="blue")

widget_invisible=Frame()
widget_invisible.grid(rowspan="7", column="0")
widget_invisible.config(width=10 ,height=350)

etiqueta.mainloop()