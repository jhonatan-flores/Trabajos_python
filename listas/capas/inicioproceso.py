import pedirdatos
while len(pedirdatos.lista)<5:
    elemento= input("ingrese la lista de elemntos:")
    pedirdatos.lista.append(elemento)
for texto in range(0,len(pedirdatos.lista)):
    if pedirdatos.lista[texto]=='disco':
        pedirdatos.palabra=pedirdatos.lista [texto]
        pedirdatos.indice=texto