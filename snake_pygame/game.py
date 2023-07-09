# game.py

import pygame
from pygame.locals import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, BACKGROUND_COLOR
from snake import Snake
from fruit import Fruit
import time  # Importa el módulo time

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake = Snake(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
fruit = Fruit(snake.body)  # Pasamos el cuerpo de la serpiente al crear la fruta

clock = pygame.time.Clock()

game_over = False  # Variable para controlar el estado del juego

score = 0  # Puntuación inicial del jugador

start_time = time.time()  # Almacena el tiempo actual al inicio del juego

while not game_over:
    clock.tick(10)  # Controla la velocidad del juego (10 fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                snake.change_direction(0, -CELL_SIZE)  # Cambia la dirección de la serpiente hacia arriba
            elif event.key == K_DOWN:
                snake.change_direction(0, CELL_SIZE)  # Cambia la dirección de la serpiente hacia abajo
            elif event.key == K_LEFT:
                snake.change_direction(-CELL_SIZE, 0)  # Cambia la dirección de la serpiente hacia la izquierda
            elif event.key == K_RIGHT:
                snake.change_direction(CELL_SIZE, 0)  # Cambia la dirección de la serpiente hacia la derecha

    snake.move()  # Mueve la serpiente

    # Verifica si la serpiente ha cruzado los límites del juego y la reposiciona en el lado opuesto
    if snake.x < 0:
        snake.x = SCREEN_WIDTH - CELL_SIZE
    elif snake.x >= SCREEN_WIDTH:
        snake.x = 0
    elif snake.y < 0:
        snake.y = SCREEN_HEIGHT - CELL_SIZE
    elif snake.y >= SCREEN_HEIGHT:
        snake.y = 0

    # Verifica si la serpiente ha colisionado consigo misma
    if snake.check_self_collision():
        game_over = True

    # Verifica si la serpiente ha alcanzado la fruta
    if snake.body[0] == (fruit.x, fruit.y):
        snake.body.append((fruit.x, fruit.y))
        fruit = Fruit(snake.body)  # Crea una nueva fruta y pasa el cuerpo de la serpiente
        score += 1  # Incrementa la puntuación en 1 cada vez que la serpiente agarra una fruta

    screen.fill(BACKGROUND_COLOR)  # Rellena la pantalla con el color de fondo

    snake.draw(screen)  # Dibuja la serpiente en la pantalla
    fruit.draw(screen)  # Dibuja la fruta en la pantalla

    # Dibuja la puntuación en la pantalla
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Calcula el tiempo transcurrido
    elapsed_time = int(time.time() - start_time)
    time_text = font.render(f"Time: {elapsed_time} s", True, (255, 255, 255))
    screen.blit(time_text, (SCREEN_WIDTH - time_text.get_width() - 10, 10))

    pygame.display.update()

# Muestra la cantidad de frutas recolectadas y el tiempo transcurrido
fruit_text = font.render(f"Frutas recolectadas: {score}", True, (255, 255, 255))
time_text = font.render(f"Tiempo: {elapsed_time} s", True, (255, 255, 255))

screen.fill(BACKGROUND_COLOR)
screen.blit(fruit_text, (SCREEN_WIDTH // 2 - fruit_text.get_width() // 2, SCREEN_HEIGHT // 2 - 40))
screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, SCREEN_HEIGHT // 2))

pygame.display.update()
time.sleep(3)  # Muestra el resultado durante 3 segundos antes de cerrar la ventana

pygame.quit()

