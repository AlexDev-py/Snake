import pygame as pg
from typing import List

import gamerules as gr
from field import Pixel

pg.init()


class Snake(list):
    def __init__(self):
        self: List[Pixel]
        super(Snake, self).__init__(
            [Pixel(17, 17, "DarkGreen"), Pixel(18, 17, "Green"), Pixel(19, 17, "Green")]
        )
        self.direction = "left"

    def draw(self, screen: pg.Surface):
        for pixel in self:
            pixel.draw(screen)

    def move(self):
        self.pop()
        self[0].color = pg.Color("Green")
        x, y = self[0].cords
        if self.direction == "left":
            x -= 1
        elif self.direction == "right":
            x += 1
        elif self.direction == "top":
            y -= 1
        elif self.direction == "down":
            y += 1
        self.insert(0, Pixel(x, y, "DarkGreen"))
