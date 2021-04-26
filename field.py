import random
from typing import List, Tuple, Union

import pygame as pg

import constants as const

pg.init()

try:
    FIELD_IMG = pg.image.load(const.FIELD_IMG)
    FIELD_IMG = pg.transform.scale(FIELD_IMG, const.DISPLAY_SIZE)
except FileNotFoundError:
    FIELD_IMG = None


def random_cords():
    return (
        random.randrange(0, const.PIXELS_COUNT),
        random.randrange(0, const.PIXELS_COUNT),
    )


class Pixel:
    def __init__(
        self, row: int, col: int, color: Union[pg.Color, str], direction: str = None
    ):
        self.cords: Tuple[int, int] = (row, col)
        cords = self.get_cords()
        self.rect = pg.Rect(
            (cords[0], cords[1], const.PIXEL_SIZE - 1, const.PIXEL_SIZE - 1)
        )
        self.color = color if isinstance(color, pg.Color) else pg.Color(color)
        self.direction = direction

    def get_cords(self) -> Tuple[int, int]:
        """ Получаем координаты клетки на экране """

        return (
            const.PIXEL_SIZE * 2 + const.PIXEL_SIZE * self.cords[0] + 1,
            const.PIXEL_SIZE * 2 + const.PIXEL_SIZE * self.cords[1] + 1,
        )

    def draw(self, screen: pg.Surface):
        """ Отображаем клетку """

        pg.draw.rect(surface=screen, color=self.color, rect=self.rect)


class Field:
    def __init__(self):
        self.apples: List[Pixel] = []  # Координаты яблок
        self._pixels: List[Pixel] = []

    def draw_grid(self, screen: pg.Surface):
        """ Отображаем края поля """

        if FIELD_IMG and const.PIXELS_COUNT == 35:
            screen.blit(FIELD_IMG, (0, 0))
        else:
            if len(self._pixels) == 0:
                self._generate_pixels()
            for pixel in self._pixels:
                pixel.draw(screen)

    def _generate_pixels(self):
        """ Создаём клетки, из которых состоит край поля """

        for i in range(-2, const.PIXELS_COUNT + 2):
            for j in range(-2, 0):
                self._pixels.append(Pixel(i, j, "Gray"))
        for i in range(-2, const.PIXELS_COUNT + 2):
            for j in range(const.PIXELS_COUNT, const.PIXELS_COUNT + 2):
                self._pixels.append(Pixel(i, j, "Gray"))
        for i in range(0, const.PIXELS_COUNT):
            for j in range(-2, 0):
                self._pixels.append(Pixel(j, i, "Gray"))
        for i in range(0, const.PIXELS_COUNT):
            for j in range(const.PIXELS_COUNT, const.PIXELS_COUNT + 2):
                self._pixels.append(Pixel(j, i, "Gray"))
