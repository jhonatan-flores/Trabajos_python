# from tkinter import*
# ventana=Tk()
# ventana.geometry("300x350")
# ventana.title("ventana edad")
# def captura_dato():
#     text=int(text_edad.get())
#     if text>=18:
#         mensaje=Label(ventana,text="eres mayor de edad :)")
#         mensaje.pack()
#     else:
#         mensaje=Label(ventana,text="eres menor de edad :(")
#         mensaje.pack()
# etiqueta=Label(ventana,text="intruduce tu edad: ")
# etiqueta.pack()
# text_edad=Entry(ventana)
# text_edad.config(bg="blue",fg="yellow")
# text_edad.pack()

# boton_capturar=Button(ventana,text="enviar",command=captura_dato)
# boton_capturar.pack()
# ventana.mainloop()

from tkinter import*
cuadro_dato=Tk()
cuadro_dato.geometry("300x350")
cuadro_dato.title("cuadro de usuario")

def comprobar_dato():
    tex1=text_usuario.get()
    contra=int(text_contraseña.get())
    if tex1==usuario and contra==contraseña:
        mensaje=Label(cuadro_dato,text="bienvenido :)")
        mensaje.pack()
    else:
        mensaje=Label(cuadro_dato,text="incorrecto :)")
        mensaje.pack()

usuario="Jhonatan"
contraseña=71470376

etiqueta=Label(cuadro_dato,text="ingresa nombre de usuario: ")
etiqueta.pack()

text_usuario=Entry(cuadro_dato)
text_usuario.config(bg="yellow",fg="black")
text_usuario.pack()

etiqueta2=Label(cuadro_dato,text="ingresa tu contaseña: ")
etiqueta2.pack()

text_contraseña=Entry(cuadro_dato)
text_contraseña.config(bg="yellow",fg="black",show="*")
text_contraseña.pack()

boton_capturar=Button(cuadro_dato,text="ingresar",command=comprobar_dato)
boton_capturar.pack()

cuadro_dato.mainloop()