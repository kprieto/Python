## Programación de Python <img src="https://brandslogos.com/wp-content/uploads/images/large/python-logo.png" alt="Python" width="50" height="50">

> [!NOTE]
> Este repositorio muestra mi experiencia en programación. Con la creación de diferentes proyectos,
> los cuáles se mencionarán detalladamente a continuación:

## Juego del Ahorcado
> El ahorcado es un clásico juego de lápiz y papel para dos o más personas.
> 
> El objetivo es adivinar una palabra secreta antes de que se complete el dibujo de un ahorcado.

**Requerimientos**

El programa cuenta con el módulo Colorama que permite darle color a la consola y es necesario instalarlo previamente. Para esto abra la terminal y ejecute el siguiente comando:
`pip install colorama`

Esta instalación debe hacerse la primera vez que use el programa.

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
7. Adivinar la palabra secreta: El jugador tendrá la opción de adivinar la palabra secreta completa.
   <img src="https://github.com/kprieto/Python/blob/main/imagenes/adivinarpalabra.png" alt="Python Adivinadr Palabra Secreta" >
8. Letras correctas: Si la letra adivinada está en la palabra secreta, se escribe en el lugar correspondiente de los guiones.
      <img src="https://github.com/kprieto/Python/blob/main/imagenes/letraadivinada.png" alt="Python Adivinar Letra" >
10. Letras incorrectas: Si la letra adivinada no está en la palabra secreta, se dibuja una parte del cuerpo del ahorcado (cabeza, cuerpo, brazos, piernas).
          <img src="https://github.com/kprieto/Python/blob/main/imagenes/letrafallada.png" alt="Python Adivinar Letra Fallada" >
    
12. Ganar o perder: El juego termina cuando se adivina toda la palabra secreta antes de completar el dibujo del ahorcado (ganas), o cuando se completa el dibujo sin adivinar la palabra secreta (pierdes).

Link: [Juego del Ahorcado](https://github.com/kprieto/Python/blob/main/juegoDelAhorcado.py). 

## Juego de Piedra, Papel o Tijera
> El juego de piedra, papel o tijera es un clásico y sencillo juego de azar para dos o más personas.
> 
> Es muy popular en todo el mundo y se utiliza a menudo para tomar decisiones rápidas y divertidas.

**¿Cómo se juega?**
1. Los gestos: Cada jugador tiene tres opciones:
   1. Piedra: Se representa cerrando el puño ✊.
   2. Papel: Se representa extendiendo la mano con todos los dedos abiertos ✋.
   3. Tijera: Se representa extendiendo el índice y el medio en forma de V ✌️.
2. Elección del gesto: La computadora seleccionara un gesto de las tres opciones al azar. El jugador deberá eligir una de los tres gestos.
3. Quién gana: Las reglas son sencillas: Se compara las dos opciones elegidas por la computadora y el jugador.
   1. Piedra aplasta tijera.
   2. Tijera corta papel.
   3. Papel envuelve a piedra.
   4. Empate: Si ambos muestran el mismo gesto.

Link: [Juego de Piedra, papel o tijera](https://github.com/kprieto/Python/blob/main/juegoPiedraPapelTijera.py).


## Juego de Trivia sobre Python
> Un juego de trivia es una excelente forma de poner a prueba tus conocimientos y divertirte al mismo tiempo.
> 
> Consiste en una serie de preguntas de opción múltiple sobre temas que contemplan a Python.

**¿Cómo se juega?**
1. Datos inciales: El jugador debe ingresar su nombre y edad. El jugador debe ser mayor de edad para iniciar el juego de la trivia.
2. Generación aleatoria: Se emplea la función random de Python para seleccionar preguntas al azar de una lista.
   <img src="https://github.com/kprieto/Python/blob/main/imagenes/pregunta.png" alt="Pregunta Ejemplo" >
   
4. Interacción con el usuario: Se utilizan funciones de entrada y salida para que el jugador introduzca sus respuestas y el programa las evalúe.
5. Conteo de puntos: Se implementa un sistema para llevar la cuenta de los aciertos y errores del jugador.
6. Puntación: Al finalizar el juego de mostrará un mensaje con la puntuación obtenida de la trivia.
   <img src="https://github.com/kprieto/Python/blob/main/imagenes/resultado.png" alt="Puntuación" >

Link: [Juego de Trivia](https://github.com/kprieto/Python/blob/main/juegoTrivia.py).

## Catálogo de Películas
> Un catálogo de películas es como una biblioteca, pero en lugar de libros, contiene información sobre películas.
> 
> Es una herramienta muy útil para organizar, buscar y descubrir nuevas películas.

**Requerimientos**

El programa cuenta con el módulo Colorama que permite darle color a la consola y es necesario instalarlo previamente. Para esto abra la terminal y ejecute el siguiente comando:
`pip install colorama`

Esta instalación debe hacerse la primera vez que use el programa.

**¿Comó se utiliza?**
1. Bienvenida al Catálogo de Películas.
2. Creación del Catálogo de Películas: El usuario deberá ingresar el nombre de un género para crear el catálogo o abrir uno ya existente.
   <img src="https://github.com/kprieto/Python/blob/main/imagenes/creacionCP.png" alt="Creación CP">   
3. Menú de opciones del Catálogo de Películas: Se mostrará un menú con las diferentes opciones que podrá el usuario realizar dentro de un Catálogo.
   <img src="https://github.com/kprieto/Python/blob/main/imagenes/menuCP.png" alt="Menú CP"> 
   
4. Despedida: Mensaje de despedida por ingresar al Catálogo de Películas.
   <img src="https://github.com/kprieto/Python/blob/main/imagenes/mensajeD.png" alt="Mensaje Despedida"> 
   
Link: [Catálogo de Películas](https://github.com/kprieto/Python/blob/main/ProyectoCatalagoPeliculas/CatalogoPelicula.py).
