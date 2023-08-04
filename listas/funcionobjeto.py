def crear_lista_frutas(lista):
    lista_fruta=[]
    for pocicion,elemento in enumerate(lista):
        fruta={
            'longitud':len(elemento),
            'valor':elemento,
            'pocicion':pocicion
        }
        lista_fruta.append(fruta)
    return lista_fruta
lista=["Manzana","Pera","Piña"]
lista_fruta=crear_lista_frutas(lista)
print(lista_fruta)