frutas=[]
indice=0
while len(frutas)<5:
    nuevafruta=input('ingrese una fruta: ')
    for fruta in frutas:
        if len(nuevafruta)==len(fruta):
            print('tiene la misma longitud ingresa otra')
    if nuevafruta in frutas:
        print('esta fruta ya existe ingrese otra')
    else:
        frutas.append(nuevafruta)

def textolargo(array):
    longitudtexto=0
    mostrarfruta=''
    for index in range(0, len(array)):
        if len(array[index]) > longitudtexto:
            longitudtexto=len(array[index])
            mostrarfruta=array[index]
            mostrarfruta=longitudtexto[index]
            indice==index
    return mostrarfruta

print(f'''
      el texto mas largo es {textolargo(frutas)}, y se encuentra el el indice{indice}
      ''')