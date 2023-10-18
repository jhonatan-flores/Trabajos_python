class Estudiante:
    alumnos=[
        {
            ID:1,
            nombre:"Jhonatan",
            apellido:"flores",
            periodo:"4to semestre",
            genero:"M"
        }
        
    ]
    def __init__(self,DNI,nombre,apellido,periodo,genero):
        self.DNI=DNI
        self.nombre=nombre
        self.apellido=apellido
        self.periodo=periodo
        self.genero=genero
    def mostrar_alumno(self):
        alumno=f''