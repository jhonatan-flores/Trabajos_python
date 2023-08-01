lista=[2,5,8,4,10]
def numeromenor(arraynumeros):
    menor=arraynumeros[0]
    for numero in arraynumeros:
        if numero < menor:
            menor=numero
    return menor
print(numeromenor(lista))


lista=[2,5,8,4,10]
def numeroMayor(arraynumeros):
    mayor=arraynumeros[0]
    for numero in arraynumeros:
        if numero>mayor:
            mayor=numero
    return mayor
print(numeroMayor(lista))
