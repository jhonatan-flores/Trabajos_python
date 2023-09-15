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