# snake.py

import pygame
from constants import SNAKE_COLOR, CELL_SIZE


class Snake:
    def __init__(self, x, y):
        """
        Inicializa una instancia de la clase Snake con una posición inicial (x, y).
        """
        self.x = x
        self.y = y
        self.dx = CELL_SIZE  # Desplazamiento en el eje x
        self.dy = 0  # Desplazamiento en el eje y
        self.body = [(x, y)]  # Lista que almacena las coordenadas de las celdas del cuerpo de la serpiente

    def move(self):
        """
        Actualiza la posición de la serpiente en función del desplazamiento dx y dy.
        Agrega una nueva celda al inicio del cuerpo y elimina la última celda para mantener la longitud constante.
        """
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))
        self.body.pop(-1)  # Elimina la última celda del cuerpo

    def change_direction(self, dx, dy):
        """
        Cambia la dirección de movimiento de la serpiente según los valores proporcionados para dx y dy.
        """
        self.dx = dx
        self.dy = dy

    def check_self_collision(self):
        """
        Verifica si la serpiente ha colisionado consigo misma.
        Devuelve True si hay celdas repetidas en el cuerpo, indicando una colisión consigo misma.
        """
        return len(self.body) != len(set(self.body))

    def draw(self, surface):
        """
        Dibuja la serpiente en la superficie especificada.
        Itera sobre las celdas del cuerpo de la serpiente y dibuja un rectángulo de color SNAKE_COLOR en la posición correspondiente.
        """
        for segment in self.body:
            pygame.draw.rect(surface, SNAKE_COLOR, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
