while True:
    jugador1 = input("Jugador 1, elige piedra, papel o tijera: ")
    jugador2 = input("Jugador 2, elige piedra, papel o tijera: ")

    if jugador1 == jugador2:
        print("Empate!")
    elif jugador1 == "piedra":
        if jugador2 == "papel":
            print("¡Jugador 2 gana! Papel envuelve piedra.")
        else:
            print("¡Jugador 1 gana! Piedra rompe tijera.")
    elif jugador1 == "papel":
        if jugador2 == "tijera":
            print("¡Jugador 2 gana! Tijera corta papel.")
        else:
            print("¡Jugador 1 gana! Papel envuelve piedra.")
    elif jugador1 == "tijera":
        if jugador2 == "piedra":
            print("¡Jugador 2 gana! Piedra rompe tijera.")
        else:
            print("¡Jugador 1 gana! Tijera corta papel.")
    else:
        print("Opción no válida. Por favor, elige piedra, papel o tijera.")

    continuar = input("¿Quieren jugar otra vez? (s/n): ")
    if continuar.lower() != "s":
        break