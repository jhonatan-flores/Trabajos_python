# AVERIGUAR FUNCIONES DE PYTHON MAS USADAS CON SUS EJEMPLOS PRACTICOS

1.- print() imprime texto en la consola.

PYTHON
print("Hola, mundo!")


2.- input(): Lee la entrada del usuario desde la consola.

PYTHON
nombre = input("Ingrese su nombre: ")


3.- len(): Calcula la longitud de una cadena o lista.

PYTHON
cadena = "Python"  
longitud = len(cadena)


4.- range(): Genera una secuencia de números.

PYTHON
numeros = list(range(1, 6))


5.- if/else: Estructuras de control condicional.
PYTHON
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

6.- for loop: Itera sobre una secuencia.
PYTHON
frutas = ["manzana", "plátano", "naranja"]
for fruta in frutas:
    print(fruta)

7.- while loop: Itera mientras se cumple una condición.
PYTHON
contador = 0
while contador < 5:
    print(contador)
    contador += 1

8.- funciones: Define funciones reutilizables.
PYTHON
def suma(a, b):
    return a + b

resultado = suma(3, 5)

9.- Listas: Estructuras de datos para almacenar elementos.
PYTHON
numeros = [1, 2, 3, 4, 5]

10.- Diccionarios: Estructuras de datos clave-valor.
PYTHON
persona = {"nombre": "Juan", "edad": 30}

11.- Métodos de cadena: Manipulación de cadenas.
PYTHON
frase = "¡Hola, mundo!"
mayusculas = frase.upper()

12.- Métodos de lista: Operaciones en listas.
PYTHON
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numeros.sort()

13.- Módulos y librerías: Importar funcionalidad adicional.
PYTHON
import math
raiz_cuadrada = math.sqrt(25)

14.- Manejo de excepciones: Captura y manejo de errores.
PYTHON
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero.")

15.- Archivo de lectura/escritura: Leer y escribir en archivos.
PYTHON
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()

## 2. Averiguar sobre entornos virtuales en python

Los entornos virtuales en Python son espacios aislados donde puedes desarrollar y ejecutar proyectos de Python de manera independiente, sin que las bibliotecas y dependencias de un proyecto afecten a otros. Aquí tienes un resumen detallado:

1. *¿Qué son los entornos virtuales?*
   Los entornos virtuales son directorios que contienen una copia independiente del intérprete de Python, junto con las bibliotecas y dependencias específicas de un proyecto. Esto permite gestionar de manera eficiente las versiones de las bibliotecas y evitar conflictos entre diferentes proyectos.

2. *Razones para usar entornos virtuales:*
   - Evitar conflictos: Cada proyecto puede tener sus propias versiones de las bibliotecas sin interferir con otros proyectos.
   - Aislamiento: Los entornos virtuales aseguran que un proyecto no se vea afectado por cambios en el sistema global de Python.
   - Versionado: Facilitan la gestión de las versiones de las bibliotecas utilizadas en un proyecto.
   - Portabilidad: Puedes compartir fácilmente un entorno virtual con otros para replicar el entorno de desarrollo.

3. *Herramientas para gestionar entornos virtuales:*
   - *virtualenv:* Es una herramienta popular que permite crear y gestionar entornos virtuales de forma sencilla.
   - *venv:* Es un módulo incorporado en Python 3.x que proporciona funcionalidad similar a virtualenv.
   - *conda:* Una herramienta de gestión de paquetes y entornos virtuales ampliamente utilizada en el ecosistema de Python científico y de análisis de datos.

4. *Creación de un entorno virtual:*
   - Utilizando `virtualenv`: Puedes crear un entorno virtual con el comando `virtualenv nombre_del_entorno`.
   - Utilizando `venv`: En Python 3.x, puedes crear un entorno virtual con `python -m venv nombre_del_entorno`.
   - Utilizando `conda`: Para usuarios de Anaconda o Miniconda, se puede crear un entorno con `conda create --name nombre_del_entorno`.

5. *Activación y desactivación:*
   - Para activar un entorno virtual, debes ejecutar un script específico dentro del directorio del entorno.
   - En sistemas Unix/Linux: `source nombre_del_entorno/bin/activate`
   - En Windows: `nombre_del_entorno\Scripts\activate`

6. *Instalación de paquetes:*
   - Dentro de un entorno virtual activado, puedes instalar paquetes específicos usando `pip`.
   - Ejemplo: `pip install nombre_del_paquete`

7. *Desactivación de un entorno virtual:*
   - Para salir de un entorno virtual, simplemente ejecuta `deactivate` en sistemas Unix/Linux o `deactivate` en Windows.

8. *Eliminación de un entorno virtual:*
   - Puedes eliminar un entorno virtual eliminando su directorio o utilizando herramientas como `virtualenvwrapper`.

9. *Requisitos y configuración de proyectos:*
   - Puedes definir las dependencias y versiones necesarias para tu proyecto en un archivo `requirements.txt`.
   - Luego, puedes recrear el entorno virtual y sus dependencias ejecutando `pip install -r requirements.txt`.

En resumen, los entornos virtuales en Python son herramientas esenciales para la gestión de proyectos, que permiten mantener un control preciso de las dependencias y aseguran que cada proyecto tenga un entorno aislado y funcional. Esto promueve un desarrollo más organizado y evita conflictos entre bibliotecas y versiones.