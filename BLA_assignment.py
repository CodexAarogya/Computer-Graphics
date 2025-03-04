import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bersenham's Line Drawing Algorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
run = True
def draw_line_dda(x1, y1, x2, y2):
    if x2 > x1:
        lx = 1
    else :
        lx = -1
    if y2 > y1:
        ly = 1
    else :
        ly = -1
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        p_k = 2*dy - dx
        
        
        while (not (x== x2)):
            if p_k < 0:
                x += lx
                y = y
                p_k += 2*dy
            else:
                x += lx
                y += ly
                p_k = p_k + 2*dy - 2*dx
           
            screen.set_at((x,y), WHITE)
           
    else:
            p_k = 2*dx - dy
            # go = True
            while (not(y== y2)):
                    if p_k < 0:
                        x = x
                        p_k += 2*dx
                    else:
                        x += lx
                        # y += ly
                        p_k = p_k + 2*dx - 2*dy
                    y += ly
                    
                    screen.set_at((x,y), WHITE)
                    
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Clear the screen
    screen.fill(BLACK)
        
    draw_line_dda(200,200,400,200)
    draw_line_dda(400,200,400,400)
    draw_line_dda(200,200,200,400)
    draw_line_dda(200,400,400,400)
    draw_line_dda(400,200,500,300)
    draw_line_dda(400,400,500,300)
    draw_line_dda(200,200,300,100)
    draw_line_dda(300,100,400,200)
    draw_line_dda(100,300,200,200)
    draw_line_dda(100,300,200,400)
    draw_line_dda(200,400,300,500)
    draw_line_dda(300,500,400,400)
    

pygame.display.flip() 
