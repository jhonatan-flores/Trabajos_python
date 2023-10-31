from tkinter import *
ventana=Tk()
ventana.title("suma y resta")
ventana.geometry("500x500")

etiqueta=Label(ventana,text='ingresa un numero: ')
etiqueta.pack()

cuadro_texto=Entry()
cuadro_texto.pack()

etiqueta=Label(ventana,text='ingresa un numero: ')
etiqueta.pack()

cuadro_texto=Entry()
cuadro_texto.pack()

etiqueta=Label(ventana,text='total:')
etiqueta.pack()

cuadro_texto=Entry()
cuadro_texto.pack()


radiosuma=Radiobutton(ventana,text="sumar",value=0)
radiosuma.pack()
radioresta=Radiobutton(ventana,text="restar",value=1)
radioresta.pack()
radiomultiplicar=Radiobutton(ventana,text="multiplicar",value=2)
radiomultiplicar.pack()
radiodividir=Radiobutton(ventana,text="dividir",value=3)
radiodividir.pack()


boton=Button(ventana,text="calcular")
boton.pack()

boton=Button(ventana,text="limpiar")
boton.pack()

ventana.mainloop()