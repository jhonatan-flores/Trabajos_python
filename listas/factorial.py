numero=int(input('ingrasa un numero: '))
factorial=1
if numero == 0:
    print('el ctorial  de 0 es 0')
else:
    for num in range (1, numero +1):
        factorial=factorial*num
    print(factorial)