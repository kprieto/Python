import random
def juegoPiedraPapeloTijera():
    opciones = ["Piedra","Papel","Tijera"]    
    terminar = True
    ganastes = 0
    perdistes = 0
    empate = 0
    while terminar:
        computadora = random.choice(opciones)
        jugador = input("Elige una opción para el juego: Piedra o Papel o Tijera o Terminar:").capitalize()
        
        if computadora == "Piedra" and jugador == "Tijera":
            print("La computadora ha ganado: Piedra aplasta la Tijera.")
            perdistes += 1
        elif computadora == "Tijera" and jugador == "Papel":
            print("La computadora ha ganado: Tijera corta el Papel.")
            perdistes += 1
        elif computadora == "Papel" and jugador == "Piedra":
            print("La computadora ha ganado: Papel envuelve la Piedra.")
            perdistes += 1
        elif jugador == "Piedra" and computadora == "Tijera":
            print("Le haz ganado a la computadora: Piedra aplasta la Tijera.")
            ganastes += 1
        elif jugador == "Tijera" and computadora == "Papel":
            print("Le haz ganado a la computadora: Tijera corta el Papel.")
            ganastes += 1            
        elif jugador == "Papel" and computadora == "Piedra":
            print("Le haz ganado a la computadora: Papel envuelve la Piedra.")
            ganastes += 1        
        elif jugador == "Terminar":
            terminar = False
        else:
            print("Es un empate.")
            empate += 1
            
    print(f"Ganastes {ganastes} veces en el juego.")
    print(f"Perdistes {perdistes} veces en el juego.")
    print(f"Hubo {empate} empates en el juego. ")
    
juegoPiedraPapeloTijera()