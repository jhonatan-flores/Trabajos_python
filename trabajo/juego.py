intentos = 0
print ("JUEGO DE AZAR....")
print ("Cual es tu nombre?...")
nombre =input("ingrsa tu nombre: ")
x = (1, 20)
print ("Hola " + nombre + ", Bienvenido a mi primer juego...." )
while intentos < 6:
    intentos = intentos + 1
print ("Elige un numero del 1 al 20")
numero = ""
numero = int (input(numero))
if numero < 21:
    print ("Tu numero es mas bajo")
    if numero > 0:
        print ("Tu numero es mas alto")
    if numero == 10:
        print ("Eres un genio....")
        print (nombre + " lo lograste con %d intentos" % (intentos))
        print ("Nos vemos....")
else:
    numero != " "
    print ("Has perdido, sera en otra oportunidad...")
    print ("Nos vemos")