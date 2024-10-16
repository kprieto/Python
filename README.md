## Programación de Python <img src="https://brandslogos.com/wp-content/uploads/images/large/python-logo.png" alt="Python" width="50" height="50">

> [!NOTE]
> Este repositorio muestra mi experiencia en programación. Con la creación de diferentes proyectos,
> los cuáles se mencionarán detalladamente a continuación:

## Juego del Ahorcado
> El ahorcado es un clásico juego de lápiz y papel para dos o más personas.
> 
> El objetivo es adivinar una palabra secreta antes de que se complete el dibujo de un ahorcado.

**¿Cómo se juega?**
1. Elección de la palabra: La computadora selecciona una palabra secreta de una lista. La cuál no será visible para el jugador.
2. Dibujo de la horca.
``` py
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)
```
3. Guiones: Se dibujan tantos guiones como letras tenga la palabra secreta, dejando espacios entre ellos para las letras.
   <img src="https://github.com/kprieto/Python/blob/main/imagenes/palabrasecreta.png" alt="Python Palabra Secreta" >

5. Adivinar letras: El jugador intentará adivinar las letras que componen la palabra secreta.
6. Adivinar la palabra secreta: El jugador tendrá la opción de adivinar la palabra secreta completa.
   <img src="https://github.com/kprieto/Python/blob/main/imagenes/adivinarpalabra.png" alt="Python Adivinadr Palabra Secreta" >
8. Letras correctas: Si la letra adivinada está en la palabra secreta, se escribe en el lugar correspondiente de los guiones.
9. Letras incorrectas: Si la letra adivinada no está en la palabra secreta, se dibuja una parte del cuerpo del ahorcado (cabeza, cuerpo, brazos, piernas).
10. Ganar o perder: El juego termina cuando se adivina toda la palabra secreta antes de completar el dibujo del ahorcado (ganas), o cuando se completa el dibujo sin adivinar la palabra secreta (pierdes).

