"""
runs the simulation and outputs a very cool pygame animation showing the movement of the animals
"""

from universe import Universe

import pygame
from win32api import GetSystemMetrics

#input parameters
DISPLAY_SIZE = int(min(GetSystemMetrics(0), GetSystemMetrics(1))*0.8)
GRID_SIZE = 50
INITIAL_PREDATORS = 50
INITIAL_PREYS = 50
ROUNDS_PER_SEC = 100

#initialise universe
u = Universe(GRID_SIZE, INITIAL_PREDATORS, INITIAL_PREYS)
TILE_SIZE = DISPLAY_SIZE / GRID_SIZE

#initialise pygame
pygame.init()
screen = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
pygame.display.set_caption('Predator prey model')
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#main pygame loop
want_to_run = True
while want_to_run:
    #EVENT HANDLING
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            want_to_run = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                want_to_run = False
                
    #GAME LOGIC
    u.move_animals()
    u.prepare_next_round()
    
    #GRAPHICS
    screen.fill(BLACK)
    for predator in u.predators:
        pygame.draw.rect(screen, RED, (predator.cell.x*TILE_SIZE, predator.cell.y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    for prey in u.preys:
        pygame.draw.rect(screen, GREEN, (prey.cell.x*TILE_SIZE, prey.cell.y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    pygame.display.flip()
    clock.tick(ROUNDS_PER_SEC)
    
pygame.quit()

