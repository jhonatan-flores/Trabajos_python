#1. importer tkinter -> libreria 
# para la creacion de interfaces grafica
from tkinter import *
#la libreria tkinter tine tres clases para la creacion de interfaces
#tk()
#tkk()
#tcl()
#2. distanciar Tk() como generador de interfas grafica
nueva_venta=Tk()
#3. frame es tambien una clase Frame() para crear un frame tengo que primero instanciarlo
menu_principal=Frame()
# montamos o inicializamos el framework haciendo uso del metodo config la asignamos 
menu_principal.pack()
menu_principal.config(width='200',height='200') 
menu_principal.config(bg='blue')
#metodo de Tk() que mantiene la ejecucion del programa de un bucle 
nueva_venta.mainloop()