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
  if letra.isalpha() and len(letra) == 1:
    return letra
  else:
    print("Solo se permite una letra.")
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
    palabra_secreta = random_palabra()
    juegoAhorcado(palabra_secreta)

def inicioJuegoAhorcado():
    bienvenidos()
    inicio = input("¿Quieres iniciar el juego del ahorcado? (s/n):").lower()
    return inicio

def limpiarPantalla():
    if os.name == "posix":
        print(chr(27) + "[2J")
        os.system ("clear")        
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        print(chr(27) + "[2J")
        os.system ("cls")        

def cuentaRegresiva(t): 
      while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        timestr = '\rIniciamos  el juego en\t' + timer
        sys.stdout.write(timestr)
        sys.stdout.flush()
        time.sleep(1)
        t -= 1 

def vidasMarcador(vidas_restantes):
    lista_vidas = []
    if vidas_restantes == 0:
        lista_vidas.append("\U0001F17E")

    for i in range(int(vidas_restantes)):
        lista_vidas.append("\U00002B55")

    return lista_vidas  

def juegoAhorcado(palabra_secreta):
  letras_ingresadas = []
  vidas_maximas = 6
  vidas = 0
  vidas_restantes = 0
  lista_vidas = []

  inicio = inicioJuegoAhorcado()

  if inicio == "s":
        while vidas < vidas_maximas:
            letra = obtener_letra()

            if letra in letras_ingresadas:
                print("Ya ingresastes estas letras antes: "+ " ".join(letras_ingresadas))
                continue

            letras_ingresadas.append(letra)

            if vidas_restantes == 0:
                lista_vidas = vidasMarcador(int(vidas_maximas))
        
            if letra not in palabra_secreta:
                vidas += 1
                vidas_restantes = vidas_maximas - vidas
                lista_vidas = vidasMarcador(int(vidas_restantes))
                imprimirDibujoAhorcado(vidas)
                dibujoVidas = " ".join(lista_vidas)
                print(f"Letra {letra} incorrecta. Te quedan {dibujoVidas}  vidas.")
            else:
                print("¡Adivinaste una letra!")

            palabra = ""
            for letra_seleccionada in palabra_secreta:
                if letra_seleccionada in letras_ingresadas:
                    palabra += letra_seleccionada
                else:
                    palabra += " _ "
            
            print("Vidas: "+" ".join(lista_vidas))
            print("Palabra: " + palabra)
            print("Ya ingresastes estas letras antes: "+ " ".join(letras_ingresadas))

            if palabra == palabra_secreta:
                print("¡Ganaste! Has adivinado la palabra.")
                reinicioJuegoAhorcado()
                break

            if vidas < vidas_maximas:
                confirmacion = input("¿Quieres adivinar la palabra? (s/n): ").lower()
                if confirmacion == "s":
                    palabra_ingresada = validar_palabra(input("Introduce la palabra: ").lower())
                    if palabra_ingresada == palabra_secreta:
                        print("¡Ganaste! Has adivinado la palabra.")
                        reinicioJuegoAhorcado()
                        break    
                    else:
                        vidas += 1
                        vidas_restantes = vidas_maximas - vidas
                        lista_vidas = vidasMarcador(int(vidas_restantes))
                        imprimirDibujoAhorcado(vidas)
                        dibujoVidas = " ".join(lista_vidas)
                        print(f"{palabra_ingresada} incorrecta. Te quedan {dibujoVidas}  vidas.")
            
            if vidas == vidas_maximas:
                print(f"¡Perdiste! La palabra secreta era: {palabra_secreta}")
                reinicioJuegoAhorcado()
  else:
    print("Gracias por jugar al ahorcado.")     





palabra_secreta = random_palabra()
juegoAhorcado(palabra_secreta)