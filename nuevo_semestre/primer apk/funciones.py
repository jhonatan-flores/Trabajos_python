from tkinter import *
from tkinter.messagebox import *
import orm
from Tabla.Usuarios import Usuarios

bd=orm.SQLiteORM("registro_estudiante")
bd.crear_tabla(Usuarios)

def limpiar(ventana):
    ventana.nombre_texto.delete(0,END)
    ventana.apellidos_texto.delete(0,END)
    ventana.celular_texto.delete(0,END)
    ventana.nombre_texto.focus()

def nuevo(ventana):
    nombre=ventana.nombre_texto.get()
    apellido=ventana.apellidos_texto.get()
    celular=ventana.celular_texto.get()
    ventana.tabla_datos.insert("",END,text=nombre,values=(apellido,celular))
    date = {
        "Nombre":nombre,
        "Apellido":apellido,
        "Celular":celular
    }
    bd.insertarUno('Usuarios',date)
    showinfo(title="Nuevo",message="Nuevo registro agregado")
    limpiar(ventana)

def eliminar(ventana):
    item_seleccionado = ventana.tabla_datos.selection()
    dato = ventana.tabla_datos.item(item_seleccionado)['text']
    print(item_seleccionado)
    if item_seleccionado:
        ventana.tabla_datos.delete(item_seleccionado)
        bd.eliminar('Usuarios',where=f'id= "{dato}"')
        showwarning(title="ELIMINAR",message="Registro elimnado")
        limpiar(ventana)
    else:
        print("Selecciona una fila del registro para eliminar.")

def actualizar(ventana):
    if ventana.nombre_texto.get()=="":
        showerror(title="SIN DATOS",message="No hay nada para actualizar")
    else:
        nombre=ventana.nombre_texto.get()
        apellidos=ventana.apellidos_texto.get()
        celular=ventana.celular_texto.get()
        regis_actualizar=ventana.tabla_datos.selection()
        date = ventana.tabla_datos.item(regis_actualizar)['text']
        mensaje=askyesno(title="Actualizar",message="Estas seguro que deseas actualizar?")
        if mensaje == True:
            limpiar(ventana)
            su_dato = {
                'Nombre':nombre,
                'Apellido':apellidos,
                'Celular':celular
                }
            ventana.tabla_datos.selection_remove(regis_actualizar)
            bd.actualizar('Usuarios',su_dato,where=f'id={date}')
            return ventana.tabla_datos.item(regis_actualizar,text=nombre,values=(apellidos,celular))
        else:
            showinfo(title="NO ACTUALIZO",message="No se  pudo actualizar ningun registro")
            limpiar(ventana)
            ventana.tabla_datos.selection_remove(regis_actualizar)

def dobleClick(ventana,event):
    elem_actualizar=ventana.tabla_datos.selection()
    captura_datos=ventana.tabla_datos.item(elem_actualizar)
    mensaje=askyesno(title="ACTUALIZAR",message="Desea actualizar los datos?")
    if mensaje == True:
        nombre=captura_datos["text"]
        apellidos=captura_datos["values"][0]
        celular=captura_datos["values"][1]
        ventana.nombre_texto.insert(0,nombre)
        ventana.apellidos_texto.insert(0,apellidos)
        ventana.celular_texto.insert(0,celular)
        ventana.tabla_datos.selection_remove(elem_actualizar)
    else:
        showinfo(title="ACTUALIZAR",message=" No has colocado ningun registro seleccionado para actualizar")
        ventana.tabla_datos.selection_remove(elem_actualizar)