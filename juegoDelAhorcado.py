#Juego del Ahorcado
import random
import os
import time
import sys
#from google.colab import output


def bienvenidos():
    print("¡¡¡Bienvenidos al Juego Del Ahorcado!!!")

def random_palabra():
    list_palabras =["zapato","casa","árbol","computadora"]
    palabra_secreta = random.choice(list_palabras).lower()
    return palabra_secreta

def obtener_letra():
      letra = validar_letra(input("Introduce una letra:").lower())
      return letra

def validar_letra(letra):
  if letra.isalpha():
    return letra
  else:
    print("No es una letra.")
    return  validar_letra(obtener_letra())

def validar_palabra(palabra):
    if palabra.isalpha():
       return palabra
    else:
      print("No es una palabra. Solo se permiten letras.")
      return validar_palabra(input("Introduce la palabra: ").lower())

def imprimirDibujoAhorcado(intentos):
    if intentos == 1:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)
    elif intentos == 2:
        print("""
                       ___
                      |   |
                      O_  |
                          |
                          |
                    ______|
        """)

    elif intentos == 3:
        print("""
                       ___
                      |   |
                     _O_  |
                          |
                          |
                    ______|
        """)

    elif intentos == 4:
      print("""
                       ___
                      |   |
                     _O_  |
                      |   |
                          |
                    ______|
        """)
    elif intentos == 5:
        print("""
                       ___
                      |   |
                     _O_  |
                      |   |
                       \  |
                    ______|
        """)
    elif intentos == 6:
        print("""
                       ___
                      |   |
                     _O_  |
                      |   |
                     / \  |
                    ______|
        """)

def reinicioJuegoAhorcado():
    cuentaRegresiva(int(5))
    limpiarPantalla()
    #output.clear()
    print("Gracias por jugar al ahorcado.")
    bienvenidos()
    palabra_secreta = random_palabra()
    juegoAhorcado(palabra_secreta)

def inicioJuegoAhorcado():
    inicio = input("¿Quieres iniciar el juego del ahorcado? (s/n):").lower()
    return inicio

def limpiarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
        print(chr(27) + "[2J")

def cuentaRegresiva(t): 
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        timestr = '\rIniciamos  el juego en\t' + timer
        sys.stdout.write(timestr)
        sys.stdout.flush()
        time.sleep(1)
        t -= 1  

def juegoAhorcado(palabra_secreta):
  letras_ingresadas = []
  intentos_maximos = 6
  intentos = 0

  inicio = inicioJuegoAhorcado()
  if inicio == "s":
    while intentos < intentos_maximos:
        letra = obtener_letra()

        if letra in letras_ingresadas:
            print("Ya ingresastes estas letras antes: "+ " ".join(letras_ingresadas))
            continue

        letras_ingresadas.append(letra)

        if letra not in palabra_secreta:
            intentos += 1
            imprimirDibujoAhorcado(intentos)
            print(f"Letra {letra} incorrecta. Te quedan {intentos_maximos - intentos} intentos.")
        else:
            print("¡Adivinaste una letra!")

        palabra = ""
        for letra_secreta in palabra_secreta:
            if letra_secreta in letras_ingresadas:
                palabra += letra_secreta
            else:
                palabra += " _ "
        print("Palabra: " + palabra)
        print("Ya ingresastes estas letras antes: "+ " ".join(letras_ingresadas))

        if palabra == palabra_secreta:
            print("¡Ganaste! Has adivinado la palabra.")
            reinicioJuegoAhorcado()
            break

        palabra_nueva = input("¿Quieres adivinar la palabra? (s/n): ").lower()
        if palabra_nueva == "s":
            palabra_ingresada = validar_palabra(input("Introduce la palabra: ").lower())
            if palabra_ingresada == palabra_secreta:
                print("¡Ganaste! Has adivinado la palabra.")
                reinicioJuegoAhorcado()
                break
            else:
                intentos += 1
                imprimirDibujoAhorcado(intentos)
                print(f"{palabra_ingresada} incorrecta. Te quedan {intentos_maximos - intentos} intentos.")


    if intentos == intentos_maximos:
        print(f"¡Perdiste! La palabra secreta era: {palabra_secreta}")
        reinicioJuegoAhorcado()
  else:
      print("Gracias por jugar al ahorcado.")


bienvenidos()
palabra_secreta = random_palabra()
juegoAhorcado(palabra_secreta)