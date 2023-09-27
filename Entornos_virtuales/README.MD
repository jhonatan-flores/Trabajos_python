# ENTORNOS VIRTUALES
## PARA CREAR UN ENTORNO VIRTUAL 
1. Nos ubicamos en la carpeta que deseamos crear un entorno virtual
```bash
cd <ruta del archivo>
ejemplo
cd nombre_carpeta/entorno_uno 
``` 
2. creamos el entorno virtual con el siguiente comando 
```bash
python -m venv <nombre de nuestro entorno virtual >
ejemlo
python -m venv mi_entorno
```
3. para activar el entorno virtual con el git bash como terminal predetermido correremos el siguiente comando para windows 
```bash
source venv/scrip/activate
```
> Nota
- en caso de que no corra en bash , podemos usar powershell
```bash
venv/scripts/activate.ps1
```
## para intalar paquetes en el entorno virtual
1. primero verificamos que no tengamos el paquete instalado y lo listamos en el siguiente comando 
```bash
pip list
```
2. luego instalaremos el siguiente comando 
```bash
pip intall<nombre del paquete>
ejemplo
pip intall pandas
``` 