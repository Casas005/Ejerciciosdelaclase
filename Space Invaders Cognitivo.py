import pygame
import sys
import random

# constantes
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 0, 0)
ENEMY_COLOR = (255, 0, 0)
ENEMY2_COLOR = (0, 255, 0)
BULLET_COLOR = (0, 0, 255)
    
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
ENEMY_WIDTH, ENEMY_HEIGHT = 25, 25
ENEMY2_WIDTH, ENEMY2_HEIGHT = 25, 25
BULLET_WIDTH, BULLET_HEIGHT = 10, 30

PLAYER_SPEED = 15
ENEMY_SPEED = 5
ENEMY2_SPEED = 5
BULLET_SPEED = 10

num = random.randint(0,1)
incorrecta = random.randint(1,100)
inco = str(incorrecta)




tablas = [["2x1", "2x2", "2x3", "2x4","2x5", "2x6", "2x7", "2x8", "2x9", "2x10" ],
            ["2", "4", "6", "8", "10", "12", "14", "16", "18", "20"],
            ["3x1", "3x2", "3x3", "3x4","3x5", "3x6", "3x7", "3x8", "3x9", "3x10" ],
           ["3", "6", "9", "12", "15", "18", "21", "24", "27", "30"],
           ["4x1", "4x2", "4x3", "4x4","4x5", "4x6", "4x7", "4x8", "4x9", "4x10" ],
            ["4", "8", "12", "16", "20", "24", "28", "32", "36", "40"],
            ["5x1", "5x2", "5x3", "5x4","5x5", "5x6", "5x7", "5x8", "5x9", "5x10" ],
           ["5", "10", "15", "20", "25", "30", "35", "40", "45", "50"],
           ["6x1", "6x2", "6x3", "6x4","6x5", "6x6", "6x7", "6x8", "6x9", "6x10" ],
            ["6", "12", "18", "24", "30", "36", "42", "48", "54", "60"],
            ["7x1", "7x2", "7x3", "7x4","7x5", "7x6", "7x7", "7x8", "7x9", "7x10" ],
           ["7", "14", "21", "28", "35", "42", "49", "56", "63", "70"],
           ["8x1", "8x2", "8x3", "8x4","8x5", "8x6", "8x7", "8x8", "8x9", "8x10" ],
            ["8", "16", "24", "32", "40", "48", "56", "64", "72", "80"],
            ["9x1", "9x2", "9x3", "9x4","9x5", "9x6", "9x7", "9x8", "9x9", "9x10" ],
           ["9", "18", "27", "36", "45", "54", "63", "72", "81", "90"]]

# pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

player_rect = pygame.Rect(WIDTH // 2 - PLAYER_WIDTH // 2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
a_rect = pygame.Rect((200, 30, 20, 20))
b_rect = pygame.Rect((600, 30, 20, 20))
font = pygame.font.Font(None, 36)

num1 = random.randrange(0,15,2)
n = random.randint(0,9)
pregunta = tablas[num1][n]
respuesta = tablas[num1+1][n]
texto = font.render(pregunta, True, WHITE)
text_resp = font.render(respuesta, True, WHITE)
text_inco = font.render(inco, True, WHITE)

# balas
bullets = []

# bloques
enemies = []
enemies2 = []


if 1 == num:
    enemy_rect = pygame.Rect((10, 60, 25, 25))
    enemies.append(enemy_rect)

    enemy2_rect = pygame.Rect((770, 50, 25, 25))
    enemies2.append(enemy2_rect)

else:
    enemy_rect = pygame.Rect((770, 50, 25, 25))
    enemies.append(enemy_rect)

    enemy2_rect = pygame.Rect((10, 60, 25, 25))
    enemies2.append(enemy2_rect)
 


score = 0



game_over = False
won_game = False 




# Cargar la imagen de fondo
background_image = pygame.image.load("D:\Javi\FIME\pogra\Python\Spacio.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Escalar la imagen al tamaño de la ventana del juego

# Cargar el archivo de sonido
pygame.mixer.init()  # Inicializa el módulo de mezcla de sonido
bullet_sound = pygame.mixer.Sound("D:\Javi\FIME\pogra\Python\Disparo.mp3")  # Reemplaza "disparo.mp3" con la ruta a tu archivo de sonido


# ciclo de juego
while not game_over:

    score = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_rect = pygame.Rect(
                    player_rect.centerx - BULLET_WIDTH // 2,
                    player_rect.top - BULLET_HEIGHT,
                    BULLET_WIDTH,
                    BULLET_HEIGHT
                )
                bullets.append(bullet_rect)
                bullet_sound.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += PLAYER_SPEED

  
    # mover balas
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        if bullet.y < 0:
            bullets.remove(bullet)

    # mover bloques
    for enemy in enemies:
        enemy.x += ENEMY_SPEED
        if enemy.right >= WIDTH or enemy.left <= 0:
            ENEMY_SPEED *= -1
            for e in enemies:
                e.y += 50
    for enemy2 in enemies2:
        enemy2.x += ENEMY2_SPEED
        if enemy2.right >= WIDTH or enemy2.left <= 0:
            ENEMY2_SPEED *= -1
            for e in enemies2:
                e.y += 50
    # choques

    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score = score + 10
            if bullet.colliderect(enemy2):
                game_over = True


    # fin de juego?
    for enemy in enemies:
        if enemy.colliderect(player_rect):
            game_over = True

    if score >= 10:
        won_game = True
        game_over = True
    # Dibujar la imagen de fondo
    screen.blit(background_image, (0, 0))
    # pantalla vacia
    screen.fill(BLACK)

    # dibujar jugador
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    play = pygame.image.load("Shutter 1.png").convert()
    play.set_colorkey([0,0,0])
    screen.blit(play, player_rect)

    # dibujar balas 
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)

    # dibujar enemigos
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)
        pygame.draw.rect(screen, ENEMY2_COLOR, enemy2)

    pygame.draw.rect(screen,ENEMY_COLOR, a_rect)
    pygame.draw.rect(screen, ENEMY2_COLOR , b_rect)

 
    # score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(texto, (350,10))
    screen.blit(text_resp, (220,30))
    screen.blit(text_inco, (620,30))
  
    # actualizar juego
    pygame.display.flip()

    # fps
    clock.tick(60)

# pantalla fin de juego
screen.fill(BLACK)
if won_game:
    won_text = font.render("¡Ganaste!", True, WHITE)
    screen.blit(won_text, (WIDTH // 2 - won_text.get_width() // 2, HEIGHT // 2 - won_text.get_height() // 2))
else:
    game_over_text = font.render("Perdiste", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
pygame.display.flip()

pygame.time.delay(2000)
pygame.quit()