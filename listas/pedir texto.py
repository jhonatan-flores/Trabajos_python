texto=input('escribe una frase: ')
def letra(array:str)->int:
    nuevo_texto=0
    for _ in list(array):
        if _ =='a':
            nuevo_texto +=1
    return nuevo_texto
print(f"El texto tiene: {letra(texto)} vocales a") 