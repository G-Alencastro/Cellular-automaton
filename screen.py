import pygame
from pygame.locals import *
from automata import *
from automata import new_gen, random_fill_grid

pygame.init()

def draw_gens(grids):
    rect_side = screen_size[0]/len(grids[0])
    pos = [0, 0]
    for grid in grids:
        for cell in grid:
            if cell:
                pygame.draw.rect(screen, (255, 255, 255), (pos, (rect_side, rect_side)))
            pos[0] += rect_side
        pos[0] = 0
        pos[1] += rect_side

screen_size = (601, 601)
screen = pygame.display.set_mode(screen_size)

fps = 10
clock = pygame.time.Clock()
grid = []
grids = []
grid = default_fill_grid(grid, 601)
while True:
    clock.tick(fps)
    screen.fill('BLACK')

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                fps += 1
            if event.key == K_DOWN:
                fps -= 1

        if event.type == QUIT:
            pygame.quit()

    grids.append(grid)
    draw_gens(grids)
    grid = new_gen(grid, rule)


    pygame.display.update()

