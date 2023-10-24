# ejercio 2
# from tkinter import *
# vent=Tk()

# cuadro_uno=Frame()
# cuadro_uno.grid(row='0',column='0')
# cuadro_uno.config(width=100,height=100)
# cuadro_uno.config(bg='blue')

# cuadro_dos=Frame()
# cuadro_dos.grid(row='0',column='1')
# cuadro_dos.config(width=100,height=100)
# cuadro_dos.config(bg='red')

# cuadro_tres=Frame()
# cuadro_tres.grid(row='1',column='0')
# cuadro_tres.config(width=200,height=100)
# cuadro_tres.config(bg='orange')

# cuadro_cuatro=Frame()
# cuadro_cuatro.grid(row='2',column='0')
# cuadro_cuatro.config(width=200,height=100)
# cuadro_cuatro.config(bg='yellow')

# cuadro_cinco=Frame()
# cuadro_cinco.grid(row='3',column='0')
# cuadro_cinco.config(width=25,height=100)
# cuadro_cinco.config(bg='pink')

# cuadro_seis=Frame()
# cuadro_seis.grid(row='3',column='1')
# cuadro_seis.config(width=25,height=100)
# cuadro_seis.config(bg='green')

# cuadro_siete=Frame()
# cuadro_siete.grid(row='3',column='2')
# cuadro_siete.config(width=25,height=100)
# cuadro_siete.config(bg='purple')

# cuadro_ocho=Frame()
# cuadro_ocho.grid(row='3',column='3')
# cuadro_ocho.config(width=25,height=100)
# cuadro_ocho.config(bg='black')

# vent.mainloop()

# widget_uno=Frame()
# widget_uno.grid(row="0",rowspan="2",column="0")
# widget_uno.config(width="100",height="200")
# widget_uno.config(bg="red")

# widget_dos=Frame()
# widget_dos.grid(row="0",column="1")
# widget_dos.config(width="100",height="100")
# widget_dos.config(bg="green")

# widget_tres=Frame()
# widget_tres.grid(row="1",column="1")
# widget_tres.config(width="100",height="100")
# widget_tres.config(bg="yellow")

# widget_cuatro=Frame()
# widget_cuatro.grid(row="2",column="0",columnspan="2")
# widget_cuatro.config(width="200",height="100")
# widget_cuatro.config(bg="blue")

from tkinter import *
# intanciar la clase Tk()
ventana=Tk()
ventana.geometry("400x500")

Widget_uno1=Frame()
Widget_uno1.grid(row="0", column="0")
Widget_uno1.config(width="400", height="50")
# Widget_uno1.config(bg="red")

# creacion de etiquetas
etiqueta=Label(ventana,text='ingresa tu nombre: ')
etiqueta.grid(row="1",column="0")
# creacion de cuadro de texto
cuadro_texto=Entry()
cuadro_texto.grid(row="2", column="0")
# usar la funcion loop para que la ventana permanesca abieta
ventana.mainloop()
