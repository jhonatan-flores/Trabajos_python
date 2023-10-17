# el nombre de la clase siempre debe ser en singular
class perro: 
    nombre='body'
    edad='2 meses'
    color='cheqche'
    raza='chusterrier'

    def ladrar(self): #siempre tiene que devolver un valor
        return "guau guau mascota"
    def corre(self,pasos): # siempre que para indicar que el primer parametro ( primer_parametro, segundo_parametro, etc) se asocia internamente con la clase,  
        responde= f"corriste {pasos}, pasos."
        return responde
## instanciar (almacenar dentro de una variavle) a mi class(clase), llamo a mi clase y lo convierto en un objeto
objeto={
    "nombre":"ruth",
    "apellido":"del rio"
}
# para acceder a mi objeto
print(objeto["nombre"])
respuesta=perro()
print(respuesta.nombre)
print(respuesta.ladrar())
print(respuesta.corre(10))
# Llama a los métodos del perro
perro.ladrar()
perro.jugar()
#crear un sistema para gestion o control de stock de productos.
# caso de uso
# historias de usuario
# producto ower
# baclog
# MVP
# prototipos de Mierda

# entidades entitis 
# la base de datos sobre lo que voy a trabajar
# averiguar formas normales(normalizacion de base de datos)
productos=[
    (

    )
]

# casos de uso
class producto:

    pass 