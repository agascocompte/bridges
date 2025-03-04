﻿# Juego basado en Manhole con Pygame

## Descripción

Este es un juego inspirado en el clásico _Manhole_, desarrollado con Pygame. En este juego, el jugador debe evitar que los personajes caigan al agua, utilizando un puente que puede moverse según la posición del ratón.

## Características

- Simulación de plataformas y puentes dinámicos.
- Personajes generados aleatoriamente que caminan y pueden caer al agua.
- Efectos visuales como burbujas, nubes y agua en movimiento.
- Elementos de flora y decoraciones en el escenario.

## Captura de Pantalla

![Imagen de ejemplo](screenshot.PNG)

## Instalación

Asegúrate de tener Python y Pygame instalados. Puedes instalar Pygame con:

```bash
pip install pygame
```

## Uso

Ejecuta el juego con el siguiente comando:

```bash
python main.py
```

## Controles

- **Clic Izquierdo**: Coloca el puente en la posición donde se hace clic.
- **ESC**: Cierra el juego.

## Despliegue web

Instalar la librería pygbag y ejecutar el comando para construir el archivo index.html:

```bash
pip install pygbag
pygbag bridges
```

Dentro del directorio `bridges` se creará el archivo index.html junto al .jar de la aplicación en `build/web`.
