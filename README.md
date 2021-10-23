<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Las canícas del juego del calamar
*[Carlos Romero]*

*[DATA PT SEP 2021, Ironhack Barcelona 2021-10-21]*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Requisitos para jugar](#requisitos)
- [Como empezar a jugar](#Como empezar a jugar)
- [Links](#links)

## Project Description
En este proyecto se ha programado un juego en Python. El juego que se ha escogido es el juego de las canicas que aparece en la serie “El juego del Calamar”. He escogido este juego porque recientemente la he visto y pensé que era un juego que se prestaba a ser programado.

## Rules
En este juego dos jugadores deben enfrentarse, cada jugador empieza con 10 canicas. En turnos los jugadores deben apostar sus canicas mientras intentan adivinar si el rival sostiene un número par o impar. En caso de adivinar correctamente, se llevará las canicas del oponente, de lo contrario perderá el número de canicas que apostó. El primer jugador que se quede sin canicas habrá perdido.

## Workflow
- Decidir el juego a crear. Se descartaron los juegos del ahorcado y el mentiroso por ser o poco estimulantes o muy complicados.
- Escribir en word el pseudocódigo de todos los pasos que haría el juego. (se puede consultar el pseudocódigo con el enlace que se aporta a drive más abajo)
- Importar módulos necesarios (random para las jugadas de la máquina y time para esperar unos segundos entre paso y paso)
- Diseñar funciones necesarias para el juego: elección de jugador y rival; aleatorio para decir quien empieza, elección de apuesta en canicas y en par/impar del rival, solicitar elección del jugador para cuantas canicas apuestan y el número impar/par del contrincante.
- Crear clase Juego para añadir todas las funciones creadas en celdas de notebook y diseñar una función con nombre “jugar” donde se especifican los pasos del juego y las interacciones del jugador con  todas las funciones.
- Exportar código clase Juego a archivo txt, completarlo y guardarlo
- Testear el juego en consola CONDA.

## Organization
Para organizar las acciones del proyecto he utilizado la técnica CAMBAN con el programa trello.

El repositorio donde se aloja el código está en https://github.com/cmromero/PR01-project-python. 

Dentro encontramos:
- README.md 
- my_code.ipynb => todo el trabajo de programación está hecho en jupyter notebook
- juego.py => código a ejecutar con Python
- .ipynb_checkpoints
- .gitignore 

## Requisitos para jugar
Tener instalado Python 3

## Como empezar a jugar
- Descargar en local el repositorio de github
- Abrir consola de comandos (p.e. Anaconda Prompt)
- Navegar con cd hasta la raíz del repositorio que hemos descargado.
- Ejecutar juego.py mediante la siguiente instrucción: “python juego.py”

## Links
[Repository]( https://github.com/cmromero/PR01-project-python)
[Slides](https://docs.google.com/presentation/d/1Hl6G5ZLDlURBEdZrBYA8ZbDWIcgo_uMF/edit?usp=sharing&ouid=104093943574938358160&rtpof=true&sd=true)  
[Trello](https://github.com/cmromero/PR01-project-python)
[Pseudocode](https://docs.google.com/document/d/1LWLBzLX0gc5wyjrPFhdib7V2wgU2GCzr/edit?usp=sharing&ouid=104093943574938358160&rtpof=true&sd=true)
