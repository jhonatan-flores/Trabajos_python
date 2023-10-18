# # if termario
# temario="soy un termario"if True else "soy falso temario"
# print (temario)
# # if normal
# if True:
#     print("soy verdad")
# else:
#     print("soy mentira")
lista_alumnos=[
    {
        "nombre":"orlando",
        "edad"  :"15",
        "hobby" :"quemarse",
        "flaca" :"melody"
    },
    {
        "nombre":"jory",
        "edad"  :"30",
        "hobby" :"voley",
        "flaca" :"maria"
    },
    {
        "nombre":"hans",
        "edad"  :"20",
        "hobby" :"aplicar",
        "flaca" :"melody"
    }
]
print(lista_alumnos)
fans_meldody=list(filter(lambda par:par["flaca"]=="melody",lista_alumnos))
print (f"los que quieren con melody{fans_meldody}")
