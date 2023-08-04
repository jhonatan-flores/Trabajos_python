nombre=['Jhonatan','Edwin','Orlando']
edad=[19,20,18]
complet=nombre+edad
def alumnos(nombre,edad):
    alumnos=[]
    for i in range(len(nombre)):
        alumno={
            'nombre':nombre[i],
            'edad':edad[i],
            'completo':f"{nombre[i]} {edad[i]}"
        }
        alumnos.append(alumno)
    return alumnos
alumnos(nombre,edad)
print(alumnos)
