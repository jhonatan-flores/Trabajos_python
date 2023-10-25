from td import *

class Tiendas_comerciales:

    def __init__(self,ruc,nombre, categoria,horario_atencion,gerente,):
        self.id=id
        self.ruc=ruc
        self.nombre=nombre
        self.categoria=categoria
        self.horario_atencion=horario_atencion
        self.gerente=gerente


    def tienda_gerente(self,td_negocios,nombre_gerente):
        respuesta=list(filter(lambda el:el["gerente"]==nombre_gerente,bd_negocios))
        return respuesta

    def tiendas_mas_categorias(self,td_negocios):
        respuesta=list(filter(lambda xd:len(xd["categoria"])>2,bd_negocios))
        return respuesta
    
    def ruc_nombre(self,td_negocios):
        respuesta=list(map(lambda par:{"ruc":par["ruc"],"nombre" :par["nombre"]},bd_negocios))
        return respuesta
    
    def eliminar_negocio(self,td_negocios,ruc):
        respuesta=list(filter(lambda el:el["ruc"]!=ruc,bd_negocios))
        return respuesta

    ## tarea
    def actualizar_negocio(self,id,clave,valor):
        ol=valor
        negocio_actualizar=list(filter(lambda obj:obj[clave]==id,negocios))[0].update({clave:valor}) 
        return 'se actualizo'

    ## otro metodo para crear un nuevo producto
    def registrar_negocio(self):
        nuevo_id=len(negocios)+1
        negocio_nuevo={
        'id':nuevo_id,
        'ruc':self.ruc,
        'nombre':self.nombre,
        'categoria':self.categoria,
        'horario_atencion':self.horario_atencion,
        'gerente':self.gerente
    }
        registro_negocio=negocios.append(negocio_nuevo)
        return 'producto registrado exitosamente'
    
    def mostrar_negocio(self, ide):
        mostrar=list(filter(lambda par:par['id']==ide,negocios))
        return f'''Aqui tienes informacion de la tienda que buscaste:  
        {mostrar}'''

    ## otro metodo para actualizar el horario de atencion
    def actualizar_horario(self, id, clave, valor):
        negocios[id-1][clave]=valor
        actu_hora=list(filter(lambda obj:obj[clave]==dato,negocios))[0].update({clave:valor}) 
        return 'se actualizo el horario'


gerente=Tiendas_comerciales()
print(gerente.tienda_gerente(negocios,"china"))

categorias=Tiendas_comerciales()
print(categorias.tiendas_mas_categorias(negocios))

ruc_nomb=Tiendas_comerciales()
print(ruc_nomb.ruc_nombre(negocios))

elim=Tiendas_comerciales()
print(elim.eliminar_negocio(negocios,675340067783))

actu=Tiendas_comerciales(675340028783,'la lechuga','bodega',{"dia":"8am-12m","tarde":"2pm-8pm"},'edwin')
print(actu.actualizar_negocio('xd','nombre','jijijja'))

print(actu.registrar_negocio())
print(actu.mostrar_negocio(11))

print(actu.actualizar_horario(1,'horario_atencion',{'dia':'7am-12pm','tarde':'3pm-9pm'}))
print(actu.mostrar_negocio(2))

