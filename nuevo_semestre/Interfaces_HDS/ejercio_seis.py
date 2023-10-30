from tkinter import *
ventana=Tk()
ventana.title("operaciones aritmeticas")
ventana.geometry("300x270")

etiqueta=Label(ventana,text='ingresa un numero: ')
etiqueta.grid(row="0",column="0")

cuadro_texto=Entry()
cuadro_texto.config(bg="blue",fg="white")
cuadro_texto.grid()

etiqueta=Label(ventana,text='ingresa un numero: ')
etiqueta.grid(row="2",column="0")

cuadro_texto=Entry()
cuadro_texto.config(bg="blue",fg="white")
cuadro_texto.grid()

etiqueta=Label(ventana,text='total:')
etiqueta.grid(row="4",column="0")

cuadro_texto=Entry()
cuadro_texto.config(bg="yellow",fg="blue")
cuadro_texto.grid()


radiosuma=Radiobutton(ventana,text="sumar",value=0)
radiosuma.grid(row="1",column="2")
radioresta=Radiobutton(ventana,text="restar",value=1)
radioresta.grid(row="0",column="2")
radiomultiplicar=Radiobutton(ventana,text="multiplicar",value=2)
radiomultiplicar.grid(row="2",column="2")
radiodividir=Radiobutton(ventana,text="dividir",value=3)
radiodividir.grid(row="4",column="2")

etiqueta=Label(ventana,text='')
etiqueta.grid(row="7",column="0")

boton=Button(ventana,text="calcular")
boton.grid
boton.grid()
etiqueta=Label(ventana,text='')
etiqueta.grid(row="9",column="0")

boton=Button(ventana,text="limpiar")
boton.grid()

ventana.mainloop()