# COMPUTER GRAPHICS FINAL PROJECT 
# BY - AAROGYA PARAJULI 
import pygame
import sys
pygame.init()

# SETTING SCREEN PARAMETERS ...
WIDTH = 900
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PING-PONG BALL")
FONT = pygame.font.SysFont("Times New Roman", int(WIDTH / 35), bold = True)
CLOCK = pygame.time.Clock()


# COLORS ...
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# INITIALIZING THE COUNTER ...
COUNTER = 0
DISP_SCORE = "Score : "

# DESIGNING BAR ...
player = pygame.Rect(WIDTH / 2 - 50, 0.95*HEIGHT  - 50 , 100, 10)

# BALL ...
ball = pygame.Rect(0 , 0 , 10, 10)
x_speed , y_speed = 1, 1

run = True
while run:

    # TAKING INPUT FROM USER ...
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_LEFT]:
        if player.left > 0:
            player.left -= 1
    if user_input[pygame.K_RIGHT]:
        if player.right < WIDTH:
            player.right += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if ball.x >= WIDTH :
        x_speed = -1
    if ball.x <= 0:
        x_speed = 1
    
    if ball.y <= 0:
        y_speed = 1
    if ball.y >= HEIGHT:
        ball.center  = ( 0 , 0)
        COUNTER = 0

    # DURING COLLISION ..
    if player.y <= ball.y <= player.y + player.height and player.x - ball.width <= ball.x <= player.x + player.width:
        y_speed = -1  
        COUNTER += 1    

    # ADJUSTING SPEEDS ...
    ball.x += x_speed 
    ball.y += y_speed 

    # RENDERING DISPLAYING TEXT ELEMENTS ...
    score = FONT.render(str(COUNTER), True, RED)
    disp = FONT.render(str(DISP_SCORE), True, RED)

    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, GREEN, player)
    pygame.draw.circle(SCREEN, WHITE, ball.center, 10)

    SCREEN.blit(disp, (WIDTH / 2 - 50 , 50))
    SCREEN.blit(score, (WIDTH / 2 + 50 , 50))


    pygame.display.flip()
    CLOCK.tick(500)
pygame.quit()
sys.exit()