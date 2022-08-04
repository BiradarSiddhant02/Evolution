import pygame
import random as rd
import Creatures as cre
import math

# def drawing(x, y):
#     pygame.draw.rect(Win, (255, 0, 0), (x, y, 10, 10))

pygame.init()

Win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("World")

world_width = 500
world_length = 500

creatures = []
x_positions = []
y_positions = []


for i in range(50):
    x = rd.randint(0, world_width)
    x_positions.append(x)
    y = rd.randint(0, world_length)
    y_positions.append(y)    
    creatures.append(cre.Creature(y, x, world_length - y, world_width - x,
                                math.sqrt(y ** 2 + (world_width - x) ** 2),
                                math.sqrt(y ** 2 + x ** 2),
                                math.sqrt((world_length - y) ** 2 + x ** 2),
                                math.sqrt((world_length - y) ** 2 + (world_width - x) ** 2), 
                                x, y, 10, 10))
    
    # drawing(x, y)

run = True
while run:
    
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Win.fill((0, 0, 0))
        
    for j, i in enumerate(creatures):
        pygame.draw.rect(Win, (255, 0, 0), (x_positions[j], y_positions[j], 10, 10))
        # print(x_positions[j], y_positions[j], i.width, i.height)
    pygame.display.update()
    
pygame.quit()