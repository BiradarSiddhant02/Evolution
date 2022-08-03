import pygame
import random as rd

pygame.init()

Win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("World")

x = rd.randint(0, 500)
y = rd.randint(0, 500)

width = 10
height = 10
v = 2

run = True
while run:
    
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Win.fill((0, 0, 0))
    pygame.draw.rect(Win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    
pygame.quit()