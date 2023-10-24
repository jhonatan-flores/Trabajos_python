from td import *
class Tiendas_comerciales:
    def tienda_gerente(self,td_negocios,nombre_gerente):
        respuesta=list(filter(lambda el:el["gerente"]==nombre_gerente,td_negocios))
        return respuesta

    def tienda_de_categorias(self,td_negocios):
        respuesta=list(filter(lambda el:len(el["categoria"])>2,td_negocios))
        return respuesta
    
    def ruc_nombre(self,td_negocios):
        respuesta=list(map(lambda el:{"ruc":el["ruc"],"nombre":el["nombre"]},td_negocios))
        return respuesta
    
    def eliminar_negocios(self,td_negocios,ruc):
        eliminar=list(filter(lambda el:el["ruc"]!=ruc,td_negocios))
        return eliminar
    def actializar_negocio(self,td_negocios):
        actualizar=list(map(lambda x:x if negocios['nombre']== negocios else negocios,td_negocios))
        return actualizar
    
    def mostrar_todo(self,td_negocios):
        respuesta=list(filter(lambda el:el["nombre"],td_negocios))
        return respuesta

# Metodo para crear un nuevo producto
#otro metodo para cambiar la hora de atencion           

gerente=Tiendas_comerciales()
print(gerente.tienda_gerente(negocios,"China"))

categorias=Tiendas_comerciales()
print(categorias.tienda_de_categorias(negocios))

ruc_nombr=Tiendas_comerciales()
print(ruc_nombr.ruc_nombre(negocios))

elim=Tiendas_comerciales()
print(elim. eliminar_negocios(negocios,675563467783))

mostrar=Tiendas_comerciales()
print(mostrar.mostrar_todo(negocios))

actualizar=Tiendas_comerciales()
print(actualizar.actializar_negocio("el telon"))