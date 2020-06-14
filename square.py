import pygame


class Square:

    def __init__(self, scrn, sizexy):
        self.scrn = scrn
        self.sizexy = sizexy

    def draw(self, x, y, clr):
        rect = pygame.Rect(x * self.sizexy[0], y * self.sizexy[1], self.sizexy[0], self.sizexy[1])
        pygame.draw.rect(self.scrn, clr, rect)
