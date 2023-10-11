# # 1. haciendo uso de la poo crear un objeto para la entidad "celular"
# class Celular: 
#     marca='samsung'
#     propietario='julian'
#     color='red'
#     version='A33'

#     def llamar(self, nombre): 
#         contacto=f"llamando a {nombre}, de tu lista de contactos."
#         return contacto
#     def escribir(self, txt, person):  
#         texto= f"tu mensaje en messenger es <<{txt}>> para {person}."
#         return texto
#     def abrir_app(self, apk):
#         app=f"abriendo {apk} en tu celular."

#         return app

# respuesta=Celular()
# print(respuesta.marca)
# print(respuesta.llamar("julian"))
# print(respuesta.escribir("hola, como estas", "juan"))
# print(respuesta.abrir_app("messenger"))

# # 2. haciendo uso de la poo crear un objeto para la entidad "vehiculo"
# class Vehiculo: 
#     marca='mercedes'
#     propietario='you'
#     color='blue'
#     serie='bens-865'

#     def acelerar(self, km): 
#         velocidad= f"vas a {km}km/h de velocidad"
#         return velocidad
#     def frenar(self,):   
#         return "frenaste"
#     def girar(self, direcc):
#         direccion=f"giraste hacia la {direcc}."
#         return direccion

# respuesta=Vehiculo()
# print(respuesta.marca)
# print(respuesta.acelerar(60))
# print(respuesta.frenar())
# print(respuesta.girar("left"))

# # 3. haciendo uso de la poo crear un objeto para la entidad "avion"
# class Avion: 
#     marca='Boeing'
#     propietario='you'
#     color='white'
#     serie='Boeing'

#     def despegar(self, km): 
#         velocidad= f"vas a {km}km/h de velocidad"
#         return velocidad
#     def aterrizar(self,):   
#         return "aterrisaste bien"
#     def girar(self, direcc):
#         direccion=f"giraste hacia la {direcc}."
#         return direccion

# respuesta=Avion()
# print(respuesta.marca)
# print(respuesta.despegar(210))
# print(respuesta.aterrizar())
# print(respuesta.girar("Right"))

# # 4. haciendo uso de la poo crear un objeto para un "heroe de dota2"
# class Heroe: 
#     nombre='axe'
#     rol='tanque'
#     fuerza=25
#     agilidad=10
#     intiligencia=10

#     def defender(self, hero): 
#         tanq= f"su rol es defender a {hero} con menos vida"
#         return tanq

# respuesta=Heroe()
# print(respuesta.nombre)
# print(respuesta.defender(2))
# #haciendo uso de la poo crear un objeto para una pc
# class PC:
#     marca='HP'
#     modelo='Pavilion'
#     procesador='Intel Core I7'
#     almacenamiento='1TB'
#     memoria='16GB'

#     def encender(self):
#         enciende=("la PC se esta encendiendo....")
#         return enciende
#     def apagar(self):
#         apagando=("la PC se est apagando....")
#         return apagando
# pc=PC()
# print(pc.encender())
# print(pc.apagar())

# # haciendo uso de la poo crear un objeto para una impresora
# class Impresora:
#     marca='HP'
#     modelo='Laser Jet'

#     def imprimir(self,texto):
#         imprim=f"Imprimiendo '{texto}' en la Impresora {self.marca} {self.modelo}"
#         return imprim
  
# impresora=Impresora()
# print(impresora.imprimir("hola mundo") )

# # haciendo uso de la poo crear un objeto para emitir una factura
# class Factura:
#     def __init__(self, numero, cliente, total):
#         self.numero = numero
#         self.cliente = cliente
#         self.total = total

#     def imprimir_factura(self):
#         print("Factura número:", self.numero)
#         print("Cliente:", self.cliente)
#         print("Total:", self.total)

# factura1 = Factura('001', "Cliente A", 100.50)

# print(factura1.imprimir_factura())
# # crear un objeto clase laptop con 2 atributos  de clase y 5 
# # atributos de instancia, devera tener hasta 3 funcionalidades como minimo 
# #crear 3 objetos instacia de clase distinto
# ###ojo:solo utilizar lo que emos echo en clase
# class Laptop:

#     # Atributos de clase
#     marca = "Acer"
#     modelo = "Aspire 5"

#     # Atributos de instancias
#     def __init__(self, color, precio, procesador, memoria, almacenamiento, pantalla):
#         self.color = color
#         self.precio = precio
#         self.procesador = procesador
#         self.memoria = memoria
#         self.almacenamiento = almacenamiento
#         self.pantalla = pantalla

#     # Funcionalidades
#     def encender(self):
#         print("La laptop se está encendiendo...")

#     def apagar(self):
#         print("La laptop se está apagando...")

#     def abrir_programa(self, programa):
#         print("Abriendo el programa " + programa)

# # Crear 3 objetos instancia de clase
# laptop_1 = Laptop("Azul", 1000, "Intel Core i5", 8, 256, 15.6)
# laptop_2 = Laptop("Rojo", 2000, "AMD Ryzen 7", 16, 512, 17.3)
# laptop_3 = Laptop("Verde", 3000, "Apple M1 Pro", 64, 1024, 16)

# # Imprimir los atributos de los objetos instancia
# print(laptop_1.color)
# print(laptop_1.precio)
# print(laptop_1.procesador)
# print(laptop_1.memoria)
# print(laptop_1.almacenamiento)
# print(laptop_1.pantalla)

# # Invocar las funcionalidades de los objetos instancia
# print(laptop_1.encender())
# print(laptop_1.apagar())
# print(laptop_1.abrir_programa("Google Chrome"))

# crear una clase de un puesto de mercado que tenga un atributos de instancia y 5 funcionalidades
# debera crear 4 instancia de la clase mercado 
# ejmpuesto mechita puesto la gringa puesto ojo de uva

class Puesto_mercado:
   nombre_lugar='mercadoNuevo'
def __init__(self,recarga,fruta,ropa,abarrote,limpieza):
    self.recarga=recarga
    self.fruta=fruta
    self.ropa=ropa
    self.abarrote=abarrote
    self.limpieza=limpieza
def recarguita(self,recarga):
    print(f'la recaga sera de: {self.recarga}')
    return print('"gracias por su rerga"') 
def fruts(self,fruta):
    print(f'a cuanto me da la {self.fruta}')
    return('¡Gracias!')
def ropas(self,ropa):
    print(f'disculpe! tiene{self.ropa}')
    return('¡Gracias!')
def abarrots(self,abarrote):
    print(f'usted vende:{self.abarrote}')
    return('¡Gracias!')
def limpiar(self,limpieza):
    print(f'que producto de limpieza quieres, quiero un {self.limpieza}')
    return('¡Gracias!')

print(puesto_mechita=Puesto_mercado('5 soles','manzana','medias','saco de azucar','ayudin'))
print(puesto_la_gringa=Puesto_mercado('10 soles','naranja','mediaspantalon','saco de aroz','patito'))
print(puesto_ojo_de_uva=Puesto_mercado('20 soles','pera','casaca','fideos por mayor','lejia'))

print(puesto_mechita.recaga())