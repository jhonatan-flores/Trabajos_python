from tkinter import *

ventana = Tk()
ventana.config(bg="white")
ventana.title("Calculadora")
entrada = Entry(ventana)
entrada.grid(row=1, columnspan=6, sticky=W + E)

i = 0
# funciones
def importar_numero(n):
    global i
    entrada.insert(i, n)
    i += 1

def operaciones(operador):
    global i
    longitud_operador = len(operador)
    entrada.insert(i, operador)
    i += longitud_operador

def limpiar():
    entrada.delete(0, END)

def eliminar_uno():
    entrada_actual = entrada.get()
    if len(entrada_actual):
        entrada_nueva = entrada_actual[:-1]
        limpiar()
        entrada.insert(0, entrada_nueva)
    else:
        limpiar()
        entrada.insert(0, 'ERROR')

def calcular():
    calcular_entrada = entrada.get()
    try:
        resultado = eval(calcular_entrada)  
        limpiar()
        entrada.insert(0, resultado)
    except Exception as e:
        limpiar()
        entrada.insert(0, "ERROR")

# botones
Button(ventana, text="1", command=lambda: importar_numero(1)).grid(row=2, column=0, sticky=W + E)
Button(ventana, text="2", command=lambda: importar_numero(2)).grid(row=2, column=1, sticky=W + E)
Button(ventana, text="3", command=lambda: importar_numero(3)).grid(row=2, column=2, sticky=W + E)
Button(ventana,text="4",command=lambda:importar_numero(4)).grid(row="3",column="0",sticky=W+E)
Button(ventana,text="5",command=lambda:importar_numero(5)).grid(row="3",column="1",sticky=W+E)
Button(ventana,text="6",command=lambda:importar_numero(6)).grid(row="3",column="2",sticky=W+E)

Button(ventana,text="7",command=lambda:importar_numero(7)).grid(row="4",column="0",sticky=W+E)
Button(ventana,text="8",command=lambda:importar_numero(8)).grid(row="4",column="1",sticky=W+E)
Button(ventana,text="9",command=lambda:importar_numero(9)).grid(row="4",column="2",sticky=W+E)

#botones part2
Button(ventana,text="ac",command=lambda:limpiar()).grid(row="5",column="0",sticky=W+E)
Button(ventana,text="0",command=lambda:importar_numero(0)).grid(row="5",column="1",sticky=W+E)
Button(ventana,text="%",command=lambda:operaciones("%")).grid(row="5",column="2",sticky=W+E)

Button(ventana,text="+",command=lambda:operaciones("+")).grid(row="2",column="3",sticky=W+E)
Button(ventana,text="-",command=lambda:operaciones("-")).grid(row="3",column="3",sticky=W+E)
Button(ventana,text="*",command=lambda:operaciones("*")).grid(row="4",column="3",sticky=W+E)
Button(ventana,text="/",command=lambda:operaciones("/")).grid(row="5",column="3",sticky=W+E)

Button(ventana,text="←",command=lambda:eliminar_uno()).grid(row="2",column="4",columnspan="2",sticky=W+E)
Button(ventana,text="exp",command=lambda:operaciones("**")).grid(row="3",column="4",sticky=W+E)
Button(ventana,text="^2",command=lambda:operaciones("**2")).grid(row="3",column="5",sticky=W+E)
Button(ventana,text="(",command=lambda:operaciones("(")).grid(row="4",column="4",sticky=W+E)
Button(ventana,text=")",command=lambda:operaciones(")")).grid(row="4",column="5",sticky=W+E)
Button(ventana, text="=", command=calcular).grid(row=5, column=4, columnspan=2, sticky=W + E)

ventana.mainloop()