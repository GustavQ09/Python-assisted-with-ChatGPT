# game.py

import pygame
from pygame.locals import *
from constants import *
from paddle import Paddle
from ball import Ball


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT))  # Crea la ventana del juego con las dimensiones especificadas en las constantes
        pygame.display.set_caption("Pong")  # Establece el título de la ventana
        self.running = True  # Indica si el juego está en ejecución o no
        self.font = pygame.font.Font(None, 36)  # Crea una fuente para el marcador del juego

        self.player_score = 0  # Puntuación del jugador
        self.ai_score = 0  # Puntuación de la IA

        self.all_sprites = pygame.sprite.Group()  # Grupo de sprites para administrar y dibujar todos los elementos del juego
        self.player_paddle = Paddle(20,
                                    HEIGHT // 2 - PADDLE_HEIGHT // 2)  # Crea la paleta del jugador en la posición inicial
        self.ai_paddle = Paddle(WIDTH - 20 - PADDLE_WIDTH,
                                HEIGHT // 2 - PADDLE_HEIGHT // 2)  # Crea la paleta de la IA en la posición inicial
        self.ball = Ball(WIDTH // 2 - BALL_WIDTH // 2,
                         HEIGHT // 2 - BALL_HEIGHT // 2)  # Crea la pelota en la posición inicial

        self.all_sprites.add(self.player_paddle)  # Agrega la paleta del jugador al grupo de sprites
        self.all_sprites.add(self.ai_paddle)  # Agrega la paleta de la IA al grupo de sprites
        self.all_sprites.add(self.ball)  # Agrega la pelota al grupo de sprites

        self.ai_move_delay = 0  # Retraso para el movimiento de la paleta de la IA
        self.ai_move_delay_max = 30  # Retraso máximo para el movimiento de la paleta de la IA

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:  # Si se detecta un evento de cierre de ventana, establece 'running' como False para salir del bucle principal
                self.running = False

        keys = pygame.key.get_pressed()  # Obtiene el estado de todas las teclas del teclado
        if keys[
            K_UP]:  # Si la tecla de flecha hacia arriba está presionada, establece la velocidad de la paleta del jugador hacia arriba
            self.player_paddle.y_speed = -PADDLE_SPEED
        elif keys[
            K_DOWN]:  # Si la tecla de flecha hacia abajo está presionada, establece la velocidad de la paleta del jugador hacia abajo
            self.player_paddle.y_speed = PADDLE_SPEED
        else:  # Si no se presionan las teclas de flecha, establece la velocidad de la paleta del jugador como cero (sin movimiento)
            self.player_paddle.y_speed = 0

    def update(self):
        self.all_sprites.update()  # Actualiza todos los sprites del juego

        # Aumentar la velocidad base de la paleta de la IA
        PADDLE_SPEED = 5 + self.player_score // 5

        if self.ai_move_delay == 0:  # Si el retraso para el movimiento de la paleta de la IA es cero
            if self.ball.rect.centery < self.ai_paddle.rect.centery:  # Si la pelota está por encima de la paleta de la IA
                self.ai_paddle.y_speed = -PADDLE_SPEED  # Establece la velocidad de la paleta de la IA hacia arriba
            elif self.ball.rect.centery > self.ai_paddle.rect.centery:  # Si la pelota está por debajo de la paleta de la IA
                self.ai_paddle.y_speed = PADDLE_SPEED  # Establece la velocidad de la paleta de la IA hacia abajo
            else:  # Si la pelota está a la altura de la paleta de la IA
                self.ai_paddle.y_speed = 0  # Establece la velocidad de la paleta de la IA como cero (sin movimiento)

            self.ai_move_delay = self.ai_move_delay_max  # Restablece el retraso para el movimiento de la paleta de la IA al valor máximo
        else:
            self.ai_move_delay -= 1  # Reduce el retraso para el movimiento de la paleta de la IA en cada actualización

        if pygame.sprite.collide_rect(self.ball,
                                      self.player_paddle):  # Si la pelota colisiona con la paleta del jugador
            self.ball.x_speed = BALL_X_SPEED  # Invierte la dirección horizontal de la pelota
        elif pygame.sprite.collide_rect(self.ball, self.ai_paddle):  # Si la pelota colisiona con la paleta de la IA
            self.ball.x_speed = -BALL_X_SPEED  # Invierte la dirección horizontal de la pelota

        if self.ball.rect.x < 0:  # Si la pelota se sale por el lado izquierdo de la pantalla
            self.ball.reset()  # Reinicia la pelota
            self.ai_score += 1  # Aumenta la puntuación de la IA
        elif self.ball.rect.x > WIDTH:  # Si la pelota se sale por el lado derecho de la pantalla
            self.ball.reset()  # Reinicia la pelota
            self.player_score += 1  # Aumenta la puntuación del jugador

        # Ajuste del movimiento del paddle de la IA
        if self.ball.y_speed > 0:  # Si la pelota se mueve hacia abajo
            self.ai_paddle.rect.centery += PADDLE_SPEED  # Mueve el paddle de la IA hacia abajo
        elif self.ball.y_speed < 0:  # Si la pelota se mueve hacia arriba
            self.ai_paddle.rect.centery -= PADDLE_SPEED  # Mueve el paddle de la IA hacia arriba

        # Limitar el movimiento del paddle de la IA dentro de los límites de la pantalla
        if self.ai_paddle.rect.top < 0:
            self.ai_paddle.rect.top = 0
        elif self.ai_paddle.rect.bottom > HEIGHT:
            self.ai_paddle.rect.bottom = HEIGHT

        if self.player_score >= 10 or self.ai_score >= 10:
            if self.player_score > self.ai_score:
                winner = "Jugador"
            else:
                winner = "IA"
            print(f"{winner} ha ganado el juego.")
            self.running = False

    def draw(self):
        self.screen.fill(BLACK)  # Limpia la pantalla con el color negro
        pygame.draw.line(self.screen, WHITE, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT],
                         1)  # Dibuja una línea blanca en el centro de la pantalla
        self.all_sprites.draw(self.screen)  # Dibuja todos los sprites del juego en la pantalla

        player_score_text = self.font.render(str(self.player_score), True,
                                             WHITE)  # Crea un texto con la puntuación del jugador
        ai_score_text = self.font.render(str(self.ai_score), True, WHITE)  # Crea un texto con la puntuación de la IA
        self.screen.blit(player_score_text,
                         (WIDTH // 2 - 50, 10))  # Dibuja el texto de la puntuación del jugador en la pantalla
        self.screen.blit(ai_score_text,
                         (WIDTH // 2 + 30, 10))  # Dibuja el texto de la puntuación de la IA en la pantalla

        pygame.display.flip()  # Actualiza la pantalla

    def run(self):
        while self.running:
            self.handle_events()  # Maneja los eventos del juego
            self.update()  # Actualiza el estado del juego
            self.draw()  # Dibuja los elementos del juego en la pantalla
            self.clock.tick(60)  # Limita la velocidad de fotogramas a 60 FPS
        pygame.quit()  # Cierra pygame y termina el juego

if __name__ == '__main__':
    game = Game()
    game.run()

