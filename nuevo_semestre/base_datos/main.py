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

def insertaraAlumno(nombre,edad):
    conn=connect("./nuevo_semestre/base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES('{nombre}',{edad})"
    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def insertaraAlumnos(lista):
    conn=connect("./nuevo_semestre/base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES(?,?)"
    cursor.executemany(sentencia,lista)
    conn.commit()
    conn.close()

if __name__=="__main__":
    # crearConexion()
    # crearTablaAlumno()
    # crearTablaCurso()
    # insertarAlumno('jory',20)
    # insertarAlumno('chinita',12)
    alum=[
        ("jorycha",50),
        ("chinita",60),
        ("nidincita",18),
        ("viuda negra",300)
    ]
    insertaraAlumnos(alum)

