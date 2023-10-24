from tkinter import*
ventana=Tk()
ventana.title("mi ventana")
ventana.geometry("500x400")

header=Frame()
header.grid(row=0,column=0,columnspan=4)
header.config(width=500,height=15,bg="red")

aside=Frame()
aside.grid(row=1,column=0,rowspan=7)
aside.config(width=15,height=385,bg="red")

etiqueta_usuario=Label(ventana,text="usuario").grid(row=1,column=0)