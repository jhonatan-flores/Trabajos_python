from tkinter import *
ventana=Tk()
ventana.config(bg="white")
ventana.title("Calculadora")
entrada=Entry(ventana).grid()
entrada.grid(row="1",columnspan="6")

Button(ventana,text="1").grid(row="2",column="0")
Button(ventana,text="2").grid(row="2",column="1")
Button(ventana,text="3").grid(row="2",column="2")
Button(ventana,text="4").grid(row="3",column="0")
Button(ventana,text="5").grid(row="3",column="1")
Button(ventana,text="6").grid(row="3",column="2")
Button(ventana,text="7").grid(row="4",column="0")
Button(ventana,text="8").grid(row="4",column="1")
Button(ventana,text="9").grid(row="4",column="2")
Button(ventana,text="0").grid(row="5",column="1")

Button(ventana,text="ac").grid(row="5",column="0")
Button(ventana,text="%").grid(row="5",column="2")

Button(ventana,text="+").grid(row="2",column="3")
Button(ventana,text="-").grid(row="3",column="3")
Button(ventana,text="*").grid(row="4",column="3")
Button(ventana,text="/").grid(row="5",column="3")

Button(ventana,text="←").grid(row="2",column="4")
Button(ventana,text="(").grid(row="4",column="4")
Button(ventana,text=")").grid(row="3",column="4")
Button(ventana,text="=").grid(row="5",column="4")


ventana.mainloop()