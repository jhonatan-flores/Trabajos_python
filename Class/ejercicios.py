# 1. crear un programa que que me pida la edad de una persona si la edad 
# es mayor o igal a 18 que me muestre un mensaje
#  "eres mayor de edad" en caso contrario que me muestre
# "eres menor de edad"
# edad=int(input('dime tu edad : '))
# if edad >=18:
#     print('eres mayor de edad')
# else:
#     print('eres menor de edad')

# 2. una tienda comercial desea hacer un descuento del 20%, crear un progra que me muestre si el cliente es acreedor 
# teniendo en cuenta los siguientes : si el cliente realiza una compar igual o mayor que 1000 soles 
# mostrar un mensaje que muestre un mesaje que diga "ganaste el descuento de 20% ahora pagaras 
# <mostrarel total de la compra menos el descuento> "
# en caso no supere los 1000 soles entonces mostrar un mesaje que diga 
# 'no aplicas al descuento <mostrar el monto de la compra>'

# precio_compra= int(input('dime el precio que compraste: '))
# if precio_compra>=1000:
#     descuento=precio_compra * 0.2
#     total_con_descuento = precio_compra-descuento
#     print("¡ Ganaste el descuento del 20% ! ahora pagaras:",total_con_descuento,"soles")
# else:
#     print("no aplicas al descuento. el monto del descuento es :",precio_compra, "soles") 

# 3. crear una programa que me pidaq 5 veces un nombre y por cada vez que lo pida muestre la cantidad de veces que ingreso el nombre
# for n in range(1,6):
#         nombre=input("ingrese un nombre: ")
#         print(f"ingresaste {n} veces el nombre")
# crear un programa que pida un numero y lo evalues con el numero premiado si el numero ingresado es el premiado el programa finalizara
# si el numero ingresaso es incorrecto el programa seguira pidiendo
# numero_premiado = 95

# while True:
#     numero_ingresado = int(input("Ingresa un número: "))

#     if numero_ingresado == numero_premiado:
#         print("¡Felicidades! Has acertado el número premiado.")
#         break 
#     else:
#         print("Número incorrecto. Inténtalo de nuevo.")

# 4. crear una funcio por cada operador arimetrico y que resiva 2 parametros y retorne el resultado de la 
# operacion, OJO. crearse un funcion que nos permita imprimir el resultado

# def mi_print(texto):
#     print(texto)

# def suma(a,b):
#     total=a+b
#     return total

# mi_print(suma(45,12))

# def resta(a,b):
#     total=a-b
#     return total

# mi_print(resta(45,12))

# def multiplicar(a,b):
#     total=a*b
#     return total

# mi_print(multiplicar(45,12))

# def dividir(a,b):
#     total=a/b
#     return total

# mi_print(dividir(45,12))

# 5. Escribe una funcion que reciba un numero entero positivo y devuelova su factorial

# def calcular_factorial(numero):
#     if numero < 0:
#         return "Solo se aceptan números positivos"
#     elif numero == 0:
#         return 1  # El factorial de 0 es 1
#     else:
#         factorial = 1
#         for i in range(1, numero + 1):
#             factorial *= i
#         return factorial

# numero = int(input("Ingresa un número: "))
# factorial_resultante = calcular_factorial(numero)

# if type(factorial_resultante) == str:
#     print(factorial_resultante)
# else:
#     print("El factorial de", numero, "es:", factorial_resultante)

## 6. Escribe una funcion que reciba un numero entero 
# positivo y devuelva su factorial

num = int(input('ingresa un numero positivo: '))

def factorial(n):
    if n == 0:
        return 1
    if num < 0: 
        print("error, ingresaste un numero negativo")
    else:
        return n * factorial(n - 1)
result = factorial(num)
print(result)

# 7. Escribir una funcion que resiva como parametros una lista de numeros y retorne una nueva 
# lista con el cuadro de cuadrado numero de la lista ingresada 
def calcular_cuadrados(lista_numeros):
    cuadrados = []  # Crear una lista vacía para almacenar los cuadrados

    for numero in lista_numeros:
        cuadrado = numero ** 2  # Calcular el cuadrado del número
        cuadrados.append(cuadrado)  # Agregar el cuadrado a la lista

    return cuadrados

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
cuadrados = calcular_cuadrados(numeros)
print(cuadrados)  # Debería imprimir [1, 4, 9, 16, 25]

# 8. Escribir un programa que reciva una cadena de careacteres y devuelva un objeto
# concada palabra que contiene y su frecuencia
def contar_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()

    # Crear un diccionario para almacenar las frecuencias
    frecuencias = {}

    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias

# Ejemplo de uso
texto = "Hola mundo, hola Python, mundo Python"
resultado = contar_palabras(texto)
print(resultado)