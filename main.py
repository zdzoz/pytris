import time

import pygame
from square import Square
from tetrominos import Tetrominos

SCREEN_X = 480
SCREEN_Y = int(SCREEN_X * (4/3))
BG_COLOR = 0x1e1e1e
print(SCREEN_Y)

def main():
    global scrn
    pygame.init()
    scrn = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    grid_size = (SCREEN_X-(SCREEN_X/3), SCREEN_Y)
    block_size = (grid_size[0]/10, grid_size[1]/20)

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        scrn.fill(BG_COLOR)

        dm = draw_grid(grid_size[0], grid_size[1], block_size)

        i = Tetrominos(scrn, block_size)
        i.t_i(1, 1)
        i.draw(0)

        i.t_i(6, 1)
        i.draw(2)

        i.t_i(1, 3)
        i.draw(1)

        i.t_i(1, 8)
        i.draw(3)


        pygame.display.flip()

    pygame.quit()


def draw_grid(sizex, sizey, bsize):
    blockx = bsize[0]
    blocky = bsize[1]
    dimensions = (int(sizex/blockx), int(sizey/blocky))
    # print(f"size: {sizex}, {sizey}\nBlock size: {blockx}, {blocky}")
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            rect = pygame.Rect(x*blockx, y*blocky, blockx, blocky)
            pygame.draw.rect(scrn, (255, 255, 255), rect, 1)
    return dimensions


if __name__ == '__main__':
    main()
