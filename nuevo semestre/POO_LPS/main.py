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