from tkinter import*
ventana=Tk()
ventana.geometry("300x350")
ventana.title("ventana suma")
def captura_dato():
    text=text_nombre.get()
    mensaje=Label(ventana,text=f"hola,{text}")
    mensaje.pack()
etiqueta=Label(ventana,text="intruduce tu nombre: ")
etiqueta.pack()
text_nombre=Entry(ventana)
text_nombre.config(bg="blue",fg="black")
text_nombre.pack()

boton_capturar=Button(ventana,text="enviar",command=captura_dato)
boton_capturar.pack()
ventana.mainloop()