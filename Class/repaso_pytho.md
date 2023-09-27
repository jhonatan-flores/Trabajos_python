# REPASO PYTHON
## 1. TIPOS DE DATOS :
### DATOS PRIMITIVOS:
#### string :
'a'-> string cadena texto

'hola'-> es tambien un string

'hola soy string'-> cadena larga

**observacion** : todo lo que esta en comillas dobles o simples es un string
- '100'
- 'False'
- "Hola"
#### numerico :
- 100-> este es un tipo de dato numerico entero
- 2.1-> este es un tipo de de dato numerico flotante float
#### boleano :
- False -> este es un tipo de dato boleano faso
- True -> este es un tipo de dato boleano verdadero
## 2. VARIABLES
es donde almacenamos uestro tipo  es **=**e datos, pero esos datos pueden cambiar o modificarse.

**como crear una variable**:
1. Darle un nombre significativo o relacionado al dato que vamos a almacenar.
2. Indicarle a que dato esta relacionado-> *asignación* es **=**
3. indicar el tipo de dato que va almacenar-> darle el dato a guardar

edad_alumno = 18
## 3. OPERADORES
### 1. operadores aritmeticos
#### suma :
- suma = 45+2
#### resta :
- resta = 30-20
#### multiplicacion : 
- multiplicacion= 10*2
#### divicion :
- divicion= 10/2
##### precedencia e operadores
### operadores de uso especial
- suma = 45+42 **el resultado sera 87**
- suma ='45' + 12 resulta **4512**
- saludo= 'hola'+'mundo'-> concatenacion **holamundo**
- saludo= 'hola' + 'mundo'-> concatenacion **hola mundo**
- saludo= ' hola'*2 -> **holahola**
## 4. DATOS ESTROCTURADOS:
son tipos de datos que ya tienen estrocturas de alguna manera
existen dos

### listas :
puede almacenar distintos tipos de datos en una sola lista

lista = ['nombre',10,false]
alumnos =[]
### objeto :
tambien al igual que las lista amacenan distintos tipos de dato pero con un orden para almacenar datos en un objetos nececitamos especificar un indice y un valor a esto se le conoce como clave->valor
alumno ={
'nombre' : 'jhonatan',
'edad' : '19',
'sexo' : 'todos los dias'
'amigos': 'hans' , 'cristhian','nadine','edwin'
}
ALUMNOS=[{},{},{}]
## 5. CONTROLES DE FLUJO :
SOLO EXISTEN 2 
### DECICIONES:

SOLOLO SE EJECUTA EL CODIGO SI LA CONDICION ES VERDERA PODEMOS HACER QUE SI LA COONDICION SEA FALSA SE EJECUTE ORO CODIGO
SINTAXIS : PRIMERO ESPECIFICAR EL CODIGO  QUE SE EJECUTARA SI CUMPLE UNA CONDICION
```PYTHON
if <condicion>:
    ##el codigo que deseamos ejecutar si la condicion es verdad 
    print('ejecuta esto')
    ##aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende del if 
```
```python
# si queremos que se ejecute un codigo en caso que sea falso 
if <condicion falsa>:
    print('solo imprime si es verdad')
else:
    print('solo imprime si es falso')
```
```python
#ejemplo
if 15 > 18:
    print('si es verdad imprime esto')
else:
    print('si es falso imprime esto')
```
```python
if 15*2 ==30:
    print('si es verdad imprime esto')
else:
    print('si es falso imprime esto')
```
### CICLOS: 
existen 2 tipos
#### iterar cuando sabes la cantidad de veces que vamos a repetir
para este caso esxiste for 

sintaxis despues de la palabra reservada for deberemos crear una variable de almacene el numero que iremos luego tendremos que indicar el rango a itera los elementos a iterar
```python
vocales= ['a','e','i','o','u']
for i in vocales:
    print(i)
```  
#### cuando no sabemos la cantidad de veces de repiter 
## funciones: 
### Existen 2 tipos de funciones:

Propias del lenguaje

Ya vienen creadas e insertadas en el lenguaje en python y estan listas para ser usadas. Estructura de uso de una funcion

tiene el nombre seguido de un parentecis.

funcion()
dentro del parentesis podremos pasarle datos que necsita la funcion para ejecutarse.

Esta es un afuncion que sirve para mostrtar datos por medio de la consola.
```python
print('hola')
len('dato')
```
Esta funcion nos permite saber la longitud de una lista o un string. Len nos devuelve un numero
```python
len('dato')
print(len([1,2,3,4,5]))
```
Esta es una funcion que se detiene a esperar que el usuario introduzca informacion. Entre parentesis podremos escribir un mensaje que indique que accion realizara el usuario.
```python
input('ingresa un dato')
```
funciones creadas
#### max
esta funcion nos muestra el numero mayor de una lista 
```python
lista=[45,12,34,65]
numero_mayor=max(lista)
print(numero_mayor)
```
#### min 
esta funcion nos muestra el numero menor de una lista
```python
lista=[20,16,37,26]
numero_menor=min(lista)
print(numero_menor)
``` 
#### de string a entero
funcion para comvertir de string a un numero entero
```python
numero_string=('28')
numero_entero=int(numero_string)
print(numero_entero)
```
#### de entero a string
funcion de combertir de un numero entero a string
```python
numero_entero=(28)
numero_string=str(numero_entero)
print(numero_string)
```
#### funcion de python que nos permita agregar elementos al final de una lista
```python
lista=[15,14,14]
elemento=[100]
lista.append(lista)
print(lista)
```
#### funcion que elimina el ultimo
```python
lista=[15,14,16]
elim=lista.pop()
eliminado=lista
print(lista)
print(eliminado)
```
#### funcion que nos permite agregar elemento en cualquier posicion de mi lista para eso se le tiene que pasar 2 parametros, primero indicarle el indice segundo el dato que se va a agregar
```python
lista_nombres=['jory','nadine','bichota']
lista_nombre.insert(1,'satan')
print(lista_nombre)
```  
#### funcion que nos permite eliminar datos de cualquier pocicion de una lista. este funcion recibe solo el elemto que deseamos eliminar(remove)
```python
lista=[4,5,6,7,8]
lista.remove(6)
print(lista)
``` 
#### funcion que nos permite dividir en una lista una cadena(split)
```python
cadena='https://github.com/NadineAtoccsaOrtiz/CLASES/tree/main/REPASO_PY'
id_url=cadena.split('_').pop()
print(id_url)
```
### 2. funciones propias
Una funcion son mini programas, tambien se le conoce como modulos o fragmentos de codigo de uso exclusivo
pasos para crear un fruncion propio
1. hacer uso de la palabra reservada def
2. definir un nombre de función que describe que tarea va a realizar
3. establecer los parámetros que resivira la función entre parentesis ()
4. establecer que valor o dato va retornar mi funcion con la palabra reservada "return"
observacion =>> tambien podemos hacer uso de la funcion print() para devolver un mensaje en nuestra funcion
existen dos tipos de funciones los que no resiven ningun parametro y los que resiven parametros
funcion sin parametros
```python
def saludo():
    print("hola este es un saludo")
# como hacemos uso de la funcion??
# nombre de la funcion y parentesis
saludo()
funcion con parametros
def mi_print(texto):
    print(texto)
```
```python
print("hola este es print de python")
mi_print("hola este es mi print creado")
def suma(a,b):
    total=a+b
    return total
```
```python
mi_print(suma(45,12)) ##=> 57
eJemplo
lista=[12,4,45,78,3,1]
mi_print(max(lista)) # =>78
```
```python
def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
            numero_mayor=numero
    return numero_mayor
mi_print(mi_max(lista))
lista=[12,4,45,78,3,1]
mi_print(min(lista)) # =>78
```
```python
def mi_min(lista):
    numero_menor=lista[0]
    for numero in lista:
        if numero < numero_menor:
            numero_menor=numero
    return numero_menor
mi_print(mi_min(lista))
funciones con muchos parámetros
def funcion(*muchos_parametros):    # el * es para poner varios parametros
    total=0
    for numero in muchos_parametros:
        total=total+numero
    return total
```
```python
print(funcion(45,78,45,415))
def datos(*args):
    nombre=args[0]
    apellido=args[1]
    edad=args[2]
    return f"mi nombre es,{nombre},{apellido} y mi edad es {edad}"

print(datos("edwin","lopez","19"))
```