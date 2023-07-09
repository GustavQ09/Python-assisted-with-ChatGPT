# ball.py

import pygame
from constants import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BALL_WIDTH, BALL_HEIGHT])  # Crea una superficie rectangular para representar la pelota
        self.image.fill(WHITE)  # Rellena la superficie con el color blanco
        self.rect = self.image.get_rect()  # Obtiene el rectángulo que delimita el área de la imagen
        self.rect.x = x  # Establece la posición inicial en el eje x
        self.rect.y = y  # Establece la posición inicial en el eje y
        self.x_speed = BALL_X_SPEED  # Establece la velocidad inicial en el eje x
        self.y_speed = BALL_Y_SPEED  # Establece la velocidad inicial en el eje y

    def update(self):
        self.rect.x += self.x_speed  # Actualiza la posición en el eje x sumando la velocidad
        self.rect.y += self.y_speed  # Actualiza la posición en el eje y sumando la velocidad

        # Rebote en los límites superior e inferior de la pantalla
        if self.rect.y < 0 or self.rect.y > HEIGHT - BALL_HEIGHT:
            self.y_speed = -self.y_speed  # Invierte la velocidad en el eje y para que la pelota rebote

    def reset(self):
        self.rect.x = WIDTH // 2  # Restablece la posición en el eje x al centro de la pantalla
        self.rect.y = HEIGHT // 2  # Restablece la posición en el eje y al centro de la pantalla
        self.x_speed = BALL_X_SPEED  # Restablece la velocidad en el eje x
        self.y_speed = BALL_Y_SPEED  # Restablece la velocidad en el eje y
