import pygame
import random as rd

pygame.init()

Win = pygame.display.set_mode((720, 720))
pygame.display.set_caption("World")



width = 6
height = 6
v = 2

run = True

    
pygame.time.delay(100)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

Win.fill((0, 0, 0))
for i in range(200):
    x = rd.randint(0, 720)
    y = rd.randint(0, 720)
    pygame.draw.rect(Win, (255, 0, 0), (x, y, width, height))
pygame.display.update()
    
