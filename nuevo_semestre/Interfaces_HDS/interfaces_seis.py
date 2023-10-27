# importar la libreria
from tkinter import *
# instanciamos nuestra clase tk()
ventana=Tk()
ventana.title("clase radiobutton")# haciendo uso del metodo title para agrgar mi titulo
ventana.geometry("400x300")#haciendo uso del metodo geometry para asignarle un tamaño fijo
# instanciar la clase label()
etiqueta=Label(ventana,text="radio buttons")#clase para crear una etiqueta 
etiqueta.config(fg="#EC5830",font=50)
etiqueta.pack()

info=IntVar()
def mostrar_radio():
    if info.get()==1:
        mensaje=Label(ventana,text="eres masculino")
        mensaje.pack()
        print(info.get())
    elif info.get()==0:
        mensaje=Label(ventana,text="eres femenino")
        mensaje.pack()
        print(info.get())
# instancioar la clase radiobutton
radiomasculino=Radiobutton(ventana,text="masculino",value=1,variable=info)
radiomasculino.pack()
radiofemenino=Radiobutton(ventana,text="femenino",value=0,variable=info)
radiofemenino.pack()

# instanciar el la clave button
boton=Button(ventana,text="enviar",command=mostrar_radio)
boton.pack()


# llamar al metodo  de tk que me permite tener percistencia al mostrar mi ventana
ventana.mainloop()