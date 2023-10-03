# 1. haciendo uso de la poo crear un objeto para la entidad "celular"
class Celular: 
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

respuesta=Celular()
print(respuesta.marca)
print(respuesta.llamar("julian"))
print(respuesta.escribir("hola, como estas", "juan"))
print(respuesta.abrir_app("messenger"))

# 2. haciendo uso de la poo crear un objeto para la entidad "vehiculo"
class Vehiculo: 
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

respuesta=Vehiculo()
print(respuesta.marca)
print(respuesta.acelerar(60))
print(respuesta.frenar())
print(respuesta.girar("left"))

# 3. haciendo uso de la poo crear un objeto para la entidad "avion"
class Avion: 
    marca='Boeing'
    propietario='you'
    color='white'
    serie='Boeing'

    def despegar(self, km): 
        velocidad= f"vas a {km}km/h de velocidad"
        return velocidad
    def aterrizar(self,):   
        return "aterrisaste bien"
    def girar(self, direcc):
        direccion=f"giraste hacia la {direcc}."
        return direccion

respuesta=Avion()
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
#haciendo uso de la poo crear un objeto para una pc
class PC:
    marca='HP'
    modelo='Pavilion'
    procesador='Intel Core I7'
    almacenamiento='1TB'
    memoria='16GB'

    def encender(self):
        enciende=("la PC se esta encendiendo....")
        return enciende
    def apagar(self):
        apagando=("la PC se est apagando....")
        return apagando
pc=PC()
print(pc.encender())
print(pc.apagar())

# haciendo uso de la poo crear un objeto para una impresora
class Impresora:
    marca='HP'
    modelo='Laser Jet'

    def imprimir(self,texto):
        imprim=f"Imprimiendo '{texto}' en la Impresora {self.marca} {self.modelo}"
        return imprim
  
impresora=Impresora()
print(impresora.imprimir("hola mundo") )

# haciendo uso de la poo crear un objeto para emitir una factura
class Factura:
    def __init__(self, numero, cliente, total):
        self.numero = numero
        self.cliente = cliente
        self.total = total

    def imprimir_factura(self):
        print("Factura número:", self.numero)
        print("Cliente:", self.cliente)
        print("Total:", self.total)

factura1 = Factura('001', "Cliente A", 100.50)

print(factura1.imprimir_factura())