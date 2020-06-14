import pygame


class Tetrominos:

    def __init__(self, scrn, sizexy):
        self.scrn = scrn
        self.sizexy = sizexy
        self.shape = []
        self.clr = 0x000

    def t_i(self, x, y):
        self.clr = 0x9be8f2
        self.shape = [

            #  0000
            #  1111
            #  0000
            #  0000
            [
                self.rect(x,     y),
                self.rect(x + 1, y),
                self.rect(x + 2, y),
                self.rect(x + 3, y)
            ],
            #  0010
            #  0010
            #  0010
            #  0010
            [
                self.rect(x + 1,     y),
                self.rect(x + 1, y + 1),
                self.rect(x + 1, y + 2),
                self.rect(x + 1, y + 3)
            ],

            #  0000
            #  0000
            #  1111
            #  0000
            [
                self.rect(x,     y + 1),
                self.rect(x + 1, y + 1),
                self.rect(x + 2, y + 1),
                self.rect(x + 3, y + 1)
            ],

            #  0100
            #  0100
            #  0100
            #  0100
            [
                self.rect(x,     y),
                self.rect(x, y + 1),
                self.rect(x, y + 2),
                self.rect(x, y + 3)
            ]
        ]

    def t_j(self):
        pass

    def t_l(self):
        pass

    def t_o(self):
        pass

    def t_s(self):
        pass

    def t_t(self):
        pass

    def t_z(self):
        pass

    def draw(self, r):
        for rect in self.shape[r]:
            pygame.draw.rect(self.scrn, self.clr, rect)

    def move(self, x, y):
        t = []
        for rect in self.shape:
            t.append(rect.move(x * self.sizexy[0], y * self.sizexy[1]))
        self.shape = t

    def rect(self, x, y):
        return pygame.Rect(x * self.sizexy[0], y * self.sizexy[1], self.sizexy[0], self.sizexy[1])
