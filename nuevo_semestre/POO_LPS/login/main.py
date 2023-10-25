## importami base de datos
from bd import * #la variable usuario de mi bd  estara disponible en este archivo
## crear clase para usuario
## esta class tendra los siguietes metodos 
## actualizar edad del usuario
## verificar si el usuario esta registrado o existe en mis registros
# validar usuario y password 
class Usuario:
    def __init__(self,dni,nombre, f_nacimiento,edad,usuario,password):
        self.id          =id
        self.dni         =dni
        self.nombre      =nombre
        self.f_nacimiento=f_nacimiento
        self.edad        =edad
        self.usuario     =usuario
        self.password    =password
    def mostrar_usuario(self,ide):
        pass
        resultado=list(filter(lambda par:par["dni"]==ide,usuarioss))
        return f"""Aqui tienes la informacion del usuario que buscaste:
    --------------------------------------------------------------------
    {resultado}"""
    def actualizar_edad(self,clave,valor):
        pass
        for Usuario in usuarioss:
            if Usuario['dni']==self.dni:
                Usuario[clave]=valor
                return 'se actualizó.'
        return 'usuario no encontrado.'
    def verificar_usuario(self,bd_usuarioss,usuario):
        pass
    def validar_usuario(self,bd_usuarioss,usuario,password):
        pass
actu=Usuario(71470376,"jhonatan","16/10/2003",None,"admin","123456789")
print(actu.actualizar_edad("edad",20))
print(actu.mostrar_usuario(71470376))