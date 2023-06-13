##Los progrmas se manejan de maneja de manera secuencial
#control de flujo
#1. CONDICIONALES
#Se reraliza algo si se cumple cierta condicion
#BLOQUES
#cuando nosotros utilicemos  cualquier control de flujo o funciones el codigo que se debe ejecutar 
#despues debera estar definida por bloques o identificaciones
##EJERCICIO
#evaluar si es menro de 17 mostrar mostrar con cana mensaje si es mayor a 18 mostrar ya como si es mayor a 40 
#mostrar ya esta usado
edad=17
if edad<18:
    print("cana no entra ni una de papel") 
if edad>18:
    print("ya come")
if edad >40:
    print("ya esta usado")
#hacer un programa que pida al usuario su DNI si la longitud del DNO es 8 que pida su nombre y lo 
#muestra por consola si la longitud del DNI  es mayor o menor a 8 que le muestre in mensaje error
#datos de entrada 
dniUsuario=input("ingrese su dni: ")
longitudDni=len(dniUsuario)
#proceso
if longitudDni==8:
#entrada
    print("""
    ingresando....
    exito!!
    """)
    nombre=input("ingresa tu nombre: ")
#proceso
    mensaje=f"""hola vienvenido, {nombre}"""
#salida de dato
    print(mensaje)
else :
    print("el dni ingresado es incorrecto")
#Hacer un programa que pida al usuario ingresar su primer apellido si su apellido tiene en como ultimos 
#caracteres las letras EZ mostrar un mensaje que diga eres casi español si los caracteres finales son es
#que diga eres casi peruano
apellido=input("ingrese su apellido paterno: ")
if apellido [-2:]=="ez":
    print("eres  casi español")
if apellido [-2:]=="es":
    print("eres casi peruano")
#hacer un programa que le pida a un usuario su dni comproube que sea de 8 digitos, si es correcto que sume
#el primer numero y el ultimo numero del dni, mostrar la suma y el resultado
dniusario=input("ingrese su dni: ")

#hacer un programa que permita que el usuario ingrrese un año y me de respuesta si es biciestro o no