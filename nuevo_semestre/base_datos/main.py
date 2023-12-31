from sqlite3 import *

def crearConexion():
    conn=connect("./nuevo_semestre/base_datos/tecnologico.db")
    conn.commit()
    conn.close()

def crearTablaAlumno():
    conn=connect("./nuevo_semestre/base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia="""
    CREATE TABLE IF NOT EXISTS Alumnos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT(250),
        edad INTEGER
    )
    """
    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def crearTablaCurso():
    conn=connect("./nuevo_semestre/base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia="""
    CREATE TABLE IF NOT EXISTS Cursos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT(250),
        id_alumno INTEGER,
        FOREIGN KEY(id_alumno) REFERENCES ALUMNOS(id)
    )
    """
    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def insertarAlumno(nombre,edad):
    conn=connect("./nuevo_semestre/base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES('{nombre}',{edad})"
    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def insertarAlumnos(lista):
    conn=connect("./nuevo_semestre/base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES(?,?)"
    cursor.executemany(sentencia,lista)
    conn.commit()
    conn.close()

def actualizarAlumno(id_alumno, nuevo_nombre, nueva_edad):
    conn = connect("./nuevo_semestre/base_datos/tecnologico.db")
    cursor = conn.cursor()

    # Assuming you have columns 'nombre' and 'edad' in your 'Alumnos' table
    sentencia = f"UPDATE Alumnos SET nombre = ?, edad = ? WHERE id = ?"
    data = (nuevo_nombre, nueva_edad, id_alumno)

    cursor.execute(sentencia, data)
    conn.commit()
    conn.close()

def eliminarAlumnoPorID(id_alumno):
    conn = connect("./nuevo_semestre/base_datos/tecnologico.db")
    cursor = conn.cursor()

    # Assuming you have a table named 'Alumnos' with a column 'id'
    sentencia = "DELETE FROM Alumnos WHERE id = ?"
    data = (id_alumno,)

    cursor.execute(sentencia, data)
    conn.commit()
    conn.close()


if __name__=="__main__":
    # crearConexion()
    # crearTablaAlumno()
    # crearTablaCurso()
    # insertarAlumno('jory',20)
    # insertarAlumno('chinita',12)
    # alum=[
    #     ("jorycha",50),
    #     ("chinita",60),
    #     ("nidincita",18),
    #     ("viuda negra",300)
    # ]
    # insertarAlumnos(alum)
    id_alumno_a_actualizar = 1  
    nuevo_nombre = "chanfaina"
    nueva_edad = 25

    actualizarAlumno(id_alumno_a_actualizar, nuevo_nombre, nueva_edad)
    # id_alumno_a_eliminar = 6  

    # eliminarAlumnoPorID(id_alumno_a_eliminar)