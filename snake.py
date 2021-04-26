import time
from typing import Union

import pygame as pg

import constants as const
from constants import LEFT, RIGHT, UP, DOWN
from field import Pixel

pg.init()


class Snake(list):
    def __init__(self):
        super(Snake, self).__init__(
            [
                Pixel(17, 17, const.SNAKE_HEAD_COLOR),
                Pixel(18, 17, const.SNAKE_BODY_COLOR),
                Pixel(19, 17, const.SNAKE_BODY_COLOR),
            ]
        )  # Начальное положение змейки
        self.direction = LEFT  # Направление движения
        self.speed = int(const.SPEED)  # Скорость змейки(клеток/секунда)

        self._last_move_time = 0  # Время, последнего движения змейки

        # Может ли змейка повернуть в данный момент
        # (для того, чтобы синхронизировать запросы пользователя с движением змейки)
        self.can_change_direction = True

    def draw(self, screen: pg.Surface):
        """ Отображает змейку """

        for pixel in self:
            pixel.draw(screen)

    def change_direction(self, value: Union[LEFT, RIGHT, UP, DOWN]) -> bool:
        """ Изменяет направление движения змейки """

        if value == LEFT and self.direction != RIGHT:
            self.direction = value
        elif value == RIGHT and self.direction != LEFT:
            self.direction = value
        elif value == UP and self.direction != DOWN:
            self.direction = value
        elif value == DOWN and self.direction != UP:
            self.direction = value
        if self.direction == value:
            self.can_change_direction = False
        return not self.can_change_direction

    def move(self):
        """ Проверка возможности движения """

        if time.time() - self._last_move_time >= 1 / self.speed:
            self._last_move_time = round(time.time(), 4)
            self.can_change_direction = True
            self._move()

    def _move(self):
        """ Перемещаем змейку """

        self.pop()  # Убираем последний элемент
        self[0].color = const.SNAKE_BODY_COLOR  # Заменяем голову, частью тела

        # Создаем новую голову
        x, y = self[0].cords  # Координаты старой головы
        if self.direction == "left":
            x -= 1
        elif self.direction == "right":
            x += 1
        elif self.direction == "up":
            y -= 1
        elif self.direction == "down":
            y += 1
        self.insert(0, Pixel(x, y, const.SNAKE_HEAD_COLOR))
