# Juego Pygame

El presente repositorio comprende los recursos y el código de un juego creado en el cojunto de módulos *pygame*. El mismo consiste en un juego 2D de plataformas con 
elementos de combate con tres niveles que presentan un tipo de desafío distinto (funcionamiento explicado a detalle más adelante).

El juego cuenta con música de fondo y efectos de sonidos. Es posible cambiar el volúmen de ambos en el menu de inicio y pausa, o directamente silenciarlos.

## Instalación

Los requisitos para correr el juego son los siguientes:

 - Python 3.9.12 o superior ([link de descarga](https://www.python.org/downloads/)).
 - Anaconda 4.14.0 ([link de descarga](https://www.anaconda.com/)).
 - Pygame (instalado por defecto con Python).
 
De ser necesario, pygame puede instalarse usando el siguiente comando:

```bash
pip install pygame
```

Una vez cumplidos los requisitos, descargar el repositorio y extraerlo en una carpeta a elección.

## Ejecución

En la carpeta en la que se extrajo el repositorio, abrir la terminal e ingresar:

```bash
python main.py
```

Este proceso deberá repetirse cada vez que uno quiera ejecutar el juego.

## Controles

*FLECHA IZQUIERDA* - Mover/Apuntar a la izquierda. 

*FLECHA DERECHA* - Mover/Apuntar a la derecha.

*BARRA ESPACIADORA* - Saltar (en la última dirección indicada).

*A* - Atacar.

*S* - Disparar proyectil.

*D* - Bloquear (Puede mantenerse apretado).

*ESCAPE* - Menú de pausa.

## Funcionamiento del juego

El propósito del jugador es eliminar a todos los enemigos en cada nivel y, de forma opcional, conseguir una puntuación alta.

Los enemigos sueltan la moneda del juego, la cual contribuye al puntuación final de cada nivel y del juego completo.
El jugador cuenta con puntos de vida, representados por la barra en la esquina superior izquierda. Los ataques enemigos y trampas reducen puntos de vida.

En caso de perder todos sus puntos, el jugador muere y el nivel se considera fallado.

El nivel cuenta con dos tipos de objetos elegidos y dispuestos de forma aleatoria. El primer tipo son gemas que contribuyen al puntuación del jugador; 
el segundo tipo, pociones que recuperan puntos de vida.

Finalmente, cada nivel cuenta con un temporizador que marca cuánto tiempo se tardó en completar. 
El jugador puede obtener multiplicadores al puntuación de cada nivel si se completa lo suficientemente rápido.

**Niveles:**

El primer nivel se completa eliminando a todos los enemigos presentes.

El segundo nivel genera enemigos cada cierto tiempo y se completa cuando ya no quedan más enemigos para generar.

El tercer nivel cuenta con un jefe y se completa cuando este es eliminado. El jefe puede invocar más enemigos pero no es necesario eliminarlos para completar el nivel 
(eliminar al jefe los elimina también).

**Tabla de puntuaciones:**

Una vez completado el tercer nivel, el jugador pasa a la pantalla de puntaciones, donde se calcula su puntuación final. También puede ver una tabla con las puntuaciones 
más altas y registrar la suya (solo se muestran las cinco más altas).

   [**Video de demostración**](https://youtu.be/RBihVMoa5IM)
