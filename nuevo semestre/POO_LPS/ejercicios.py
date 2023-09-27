# 1. haciendo uso de la poo crear un objeto para la entidad "celular"
class celular: 
    marca='samsung'
    propietario='julian'
    color='red'
    version='A33'

    def llamar(self, nombre): 
        contacto=f"llamando a {nombre}, de tu lista de contactos."
        return contacto
    def escribir(self, txt, person):  
        texto= f"tu mensaje en messenger es <<{txt}>> para {person}."
        return texto
    def abrir_app(self, apk):
        app=f"abriendo {apk} en tu celular."

        return app

respuesta=celular()
print(respuesta.marca)
print(respuesta.llamar("julian"))
print(respuesta.escribir("hola, como estas", "juan"))
print(respuesta.abrir_app("messenger"))

# 2. haciendo uso de la poo crear un objeto para la entidad "vehiculo"
class vehiculo: 
    marca='mercedes'
    propietario='you'
    color='blue'
    serie='bens-865'

    def acelerar(self, km): 
        velocidad= f"vas a {km}km/h de velocidad"
        return velocidad
    def frenar(self,):   
        return "frenaste"
    def girar(self, direcc):
        direccion=f"giraste hacia la {direcc}."
        return direccion

respuesta=vehiculo()
print(respuesta.marca)
print(respuesta.acelerar(60))
print(respuesta.frenar())
print(respuesta.girar("left"))

# 3. haciendo uso de la poo crear un objeto para la entidad "avion"
class avion: 
    marca='Boeing'
    propietario='you'
    color='white'
    serie='Boeing-865'

    def despegar(self, km): 
        velocidad= f"vas a {km}km/h de velocidad"
        return velocidad
    def aterrizar(self,):   
        return "aterrisaste"
    def girar(self, direcc):
        direccion=f"giraste hacia la {direcc}."
        return direccion

respuesta=avion()
print(respuesta.marca)
print(respuesta.despegar(210))
print(respuesta.aterrizar())
print(respuesta.girar("Right"))

# 4. haciendo uso de la poo crear un objeto para un "heroe de dota2"
class Heroe: 
    nombre='axe'
    rol='tanque'
    fuerza=25
    agilidad=10
    intiligencia=10

    def defender(self, hero): 
        tanq= f"su rol es defender a {hero} con menos vida"
        return tanq

respuesta=Heroe()
print(respuesta.nombre)
print(respuesta.defender(2))


# leer tkinter, libreriade python para la creacion de interfaces graficas