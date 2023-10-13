# importamos tkinter
from tkinter import *
# instanciar la clase tk()
ventana=Tk()

#creo mis dos widget de orden superior con la clase frame()
#instancio mi primer widget
Widget_uno=Frame()
#usar metodo para montar el frame
Widget_uno.grid(row='0',column='0')
Widget_uno.config(width=100,height=100)
Widget_uno.config(bg='blue')

widget_dos=Frame()
widget_dos.grid(row='2',column='0')
widget_dos.config(width=100,height=100)
widget_dos.config(bg='yellow')


ventana.mainloop()