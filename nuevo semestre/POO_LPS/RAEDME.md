# programacion orientado a objeto
## "en ingles seria object orient programing(OOP)"
- es un paradigma de programacion
>**Paradigma**: es un modelo, patron o ejemplo que deve seguir
#### POO : es un modelo de como pogramar
>**Objetivo** - el objetivo es organizar el codigo de manera que se asemeje de como lo vemos en la vida real 

se basa en objetos 

>poo un objeto es toda entidad  que se pueda escrivir atravez de **atributos** y **funciones** que puede realizar la entidad

## atributos de clase y de instancia
```python
class Celular:
    # atributos de tipo clase
    # que son iguale para todos los objetos
    #que se creen
    familia='Smart Phone'
    # atributos de instancia
    # son atrivutos propias del objeto
    # creamos una funcion nicializandolo
    def __init__(self,marca,modelo,imei,nrocelular):
        self.marca=marca
        self.modelo=modelo
        self.imei=imei
        self.nrocelular=nrocelular
    #funcionalidades
    def Llamar(self,destino):
        return f'llamando a (destino)'
#objeto celular jory
llamandoJory=Celular('poco','x5','67652676412345','987654321')
print(llamandoJory.marca)
print(llamandoJory.familia)
print(llamandoJory.Llamar('china'))
#objeto celular nadine
llamandoNadine=Celular('alcatel','basico','7775734636','978654321')
print(llamandoJory.marca)
print(llamandoJory.familia)
print(llamandoJory.Llamar('ollanta')) 
```