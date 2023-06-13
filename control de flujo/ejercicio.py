op=int(input("ingrese 1=suma 0 2=resta: "))
n1= int(input("ingreseN1:"))
n2=int(input("ingrese n2"))
if op==1:
    print("suma: ", n1+n2,"  :)")
elif op==2:
    print("resta: ",n1-n2," :(")
else:
    print("error al seleccionar la operacion")