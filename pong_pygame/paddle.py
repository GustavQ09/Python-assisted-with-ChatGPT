import pygame
from constants import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])  # Crea una superficie rectangular para representar la paleta
        self.image.fill(WHITE)  # Rellena la superficie con el color blanco
        self.rect = self.image.get_rect()  # Obtiene el rectángulo que delimita el área de la imagen
        self.rect.x = x  # Establece la posición inicial en el eje x
        self.rect.y = y  # Establece la posición inicial en el eje y
        self.y_speed = 0  # Establece la velocidad inicial en el eje y

    def update(self):
        self.rect.y += self.y_speed  # Actualiza la posición en el eje y sumando la velocidad

        # Limita la posición de la paleta dentro de los límites de la pantalla
        if self.rect.y < 0:
            self.rect.y = 0  # Si la paleta se sale por arriba, se ajusta su posición al límite superior
        if self.rect.y > HEIGHT - PADDLE_HEIGHT:
            self.rect.y = HEIGHT - PADDLE_HEIGHT  # Si la paleta se sale por abajo, se ajusta su posición al límite inferior

