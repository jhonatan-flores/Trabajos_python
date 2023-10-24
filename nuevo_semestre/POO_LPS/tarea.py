from td import *
class Tiendas_comerciales:
    def tienda_gerente(self,td_negocios,nombre_gerente):
        respuesta=list(filter(lambda el:el["gerente"]==nombre_gerente,td_negocios))
        return respuesta

    def tiendas_mas_categorias(self,td_negocios):
        respuesta=list(filter(lambda el:len(el["categoria"])>2,td_negocios))
        return respuesta
    
    def ruc_nombre(self,td_negocios):
        respuesta=list(map(lambda el:{"ruc":el["ruc"],"nombre":el["nombre"]},td_negocios))
        return respuesta
    def eliminar_negocio(self,td_negocios,ruc):
        eliminar=list(filter(lambda el:el["ruc"]!=ruc,td_negocios))
        return eliminar
    def actializar_negocio():
        pass
    
    def mostrar_todo(self,negocios):
        pass

gerente=Tiendas_comerciales()
print(gerente.tienda_gerente(negocios,"China"))

categorias=Tiendas_comerciales()
print(categorias.tiendas_mas_categorias(negocios))

ruc_nombr=Tiendas_comerciales()
print(ruc_nombr.ruc_nombre(negocios))

elim=Tiendas_comerciales
print(elim.eliminar_negocio(negocios,"675346007783"))