# fruit.py

import random
import pygame
from constants import FRUIT_COLOR, CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT


class Fruit:
    def __init__(self, snake_body):
        """
        Inicializa una instancia de la clase Fruit y genera una posición aleatoria para la fruta.
        La posición generada no debe estar en las mismas coordenadas que las celdas del cuerpo de la serpiente.
        """
        self.generate_position(snake_body)

    def generate_position(self, snake_body):
        """
        Genera una posición aleatoria para la fruta dentro de los límites del juego.
        La posición generada no debe estar en las mismas coordenadas que las celdas del cuerpo de la serpiente.
        """
        max_x = (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE  # Máximo valor de x para la posición de la fruta
        max_y = (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE  # Máximo valor de y para la posición de la fruta

        while True:
            self.x = random.randint(0, max_x) * CELL_SIZE  # Genera una coordenada x aleatoria
            self.y = random.randint(0, max_y) * CELL_SIZE  # Genera una coordenada y aleatoria
            if (self.x, self.y) not in snake_body:  # Verifica que la posición generada no esté en las celdas del cuerpo de la serpiente
                break

    def draw(self, surface):
        """
        Dibuja la fruta en la superficie especificada.
        """
        pygame.draw.rect(surface, FRUIT_COLOR, (self.x, self.y, CELL_SIZE, CELL_SIZE))  # Dibuja un rectángulo de color FRUIT_COLOR en la posición de la fruta

