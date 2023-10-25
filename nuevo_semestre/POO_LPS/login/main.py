## importami base de datos
from bd import * #la variable usuario de mi bd  estara disponible en este archivo
## crear clase para usuario
## esta class tendra los siguietes metodos 
## actualizar edad del usuario
## verificar si el usuario esta registrado o existe en mis registros
# validar usuario y password 
class usuario:
    def __init__(self,dni,nombre, f_nacimiento,edad,usuario,password):
        self.id          =id
        self.dni         =dni
        self.nombre      =nombre
        self.f_nacimiento=f_nacimiento
        self.edad        =edad
        self.usuario     =usuario
        self.password    =password
    
    def actualizar_edad(self,bd_usuarioss,edad):
        pass
        edad_actual=list()
        return f"""
    la edad actual es: {edad_actual}
    """
    def verificar_usuario(self,bd_usuarioss,usuario):
        pass
    def validar_usuario(self,bd_usuarioss,usuario,password):
        pass