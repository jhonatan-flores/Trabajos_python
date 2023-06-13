numerjugar=int(input("Ingrese la cantidadde jugadores: "))
if numerjugar==2:
 print("Inicia el juego de piedra,papel y  tijeras")
 nombre1=input("Ingresa tu nombre jugador 1: ")
 nombre2=input("Ingresa tu nombre jugador 2: ")
 jugador1=input(f"{nombre1} ingrese entre piedra,papel o tijera: ")
 jugador2=input(f"{nombre2} ingrese entre piedra,papel o tijera: ")
 jugadores=jugador1 and jugador2
 match jugadores:
    case jugadores if jugador1=="piedra" and jugador2=="tijera":
        print(f"Gana {nombre1}")
    case jugadores if jugador1=="papel" and jugador2=="piedra":
        print(f"Gana {nombre1}")
    case jugadores if jugador1=="tijera" and jugador2=="papel":
        print(f"Gana {nombre1}")
    case jugadores if jugador1=="piedra" and jugador2=="piedra":
        print("Empate")
    case jugadores if jugador1=="papel" and jugador2=="papel":
        print("Empate")
    case jugadores if jugador1=="tijera" and jugador2=="tijera":
        print("Empate")
    case jugadores if jugador2=="piedra" and jugador1=="tijera":
        print(f"Gana {nombre2}")
    case jugadores if jugador2=="papel" and jugador1=="piedra":
        print(f"Gana {nombre2}")
    case jugadores if jugador2=="tijera" and jugador1=="papel":
        print(f"Gana {nombre2}") 
else:
 print("La cantidad de jugadores es incorrecta")