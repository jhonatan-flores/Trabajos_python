condicion=2
while condicion<21:
 print(condicion)
 condicion=condicion+2

edad=0
while edad != 20:
  edad=int(input("ingrese edad: "))
  
nombre= "" 
while nombre != "si":
    nombre=input("ingrese su nombre: ")

while True:
  nombre=input("como te llamas: ")
  if nombre == "si":
    break
  
while True:
  bingo=input("ingrese el numero ganador: ")
  if bingo == "":
    print("primer intento")
  if bingo == "":
    print("segundo intento")
  if bingo == "2":
    break
  else:
    print("perdiste la opotunidad")
