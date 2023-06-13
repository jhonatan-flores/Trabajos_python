listanum=(1,2,3,4,5,6,7,8,9,10)
def numeros_par(lista):
    nueva_lista=[]
    for _,num in enumerate(lista):
        if num%2==0:
            nueva_lista.append(num)
    return nueva_lista
print(numeros_par(listanum))

