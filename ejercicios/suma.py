lista=[2,5,8,4,2]
def sumadenumeros(arraynumeros):
    totalsuma=0
    for numero in arraynumeros:
        totalsuma +=numero
    return totalsuma
print(sumadenumeros(lista))