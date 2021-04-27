import time
from typing import Union, List

import pygame as pg

import constants as const
from constants import LEFT, RIGHT, UP, DOWN
from field import Pixel

pg.init()


def other_direction(
    direction: Union[LEFT, RIGHT, UP, DOWN]
) -> Union[LEFT, RIGHT, UP, DOWN]:
    """ Получаем противоположное направление от `direction` """

    if direction == RIGHT:
        return LEFT
    elif direction == LEFT:
        return RIGHT
    elif direction == UP:
        return DOWN
    elif direction == DOWN:
        return UP


class Snake(list):
    def __init__(self):
        center = const.PIXELS_COUNT // 2
        super(Snake, self).__init__(
            [
                Pixel(center - 1, center, const.SNAKE_HEAD_COLOR, LEFT),
                Pixel(center, center, const.SNAKE_BODY_COLOR, LEFT),
                Pixel(center + 1, center, const.SNAKE_BODY_COLOR, LEFT),
            ]
        )  # Начальное положение змейки
        self.direction = LEFT  # Направление движения
        self.speed = int(const.SPEED)  # Скорость змейки(клеток/секунда)

        self._last_move_time = 0  # Время, последнего движения змейки

        # Может ли змейка повернуть в данный момент
        # (для того, чтобы синхронизировать запросы пользователя с движением змейки)
        self.can_change_direction = True

        # Нужно ли увеличить змейку и на сколько
        self._need_enlarge = 0

    def draw(self, screen: pg.Surface):
        """ Отображает змейку """

        for pixel in self[::-1]:
            pixel.draw(screen)

    def change_direction(self, value: Union[LEFT, RIGHT, UP, DOWN]) -> bool:
        """ Изменяет направление движения змейки """

        if value != other_direction(self.direction):
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

        if self._need_enlarge == 0:
            self.pop()  # Убираем последний элемент
        else:
            self._need_enlarge -= 1
        self[0].color = const.SNAKE_BODY_COLOR  # Заменяем голову, частью тела

        # Создаем новую голову
        x, y = self[0].cords  # Координаты старой головы
        if self.direction == LEFT:
            x -= 1
        elif self.direction == RIGHT:
            x += 1
        elif self.direction == UP:
            y -= 1
        elif self.direction == DOWN:
            y += 1
        self.insert(0, Pixel(x, y, const.SNAKE_HEAD_COLOR, self.direction))

    def eat(self):
        """ Змейка скушала яблоко """

        # Меняем направление
        self.direction = other_direction(self[-1].direction)

        # Разворачиваем змейку
        snake: List[Pixel] = self.copy()  # Копируем
        self.clear()  # Очищаем
        # Создаем голову
        self.append(Pixel(*snake[-1].cords, const.SNAKE_HEAD_COLOR, self.direction))
        self.extend(
            [
                Pixel(*pixel.cords, pixel.color, other_direction(pixel.direction))
                for pixel in snake[1:-1][::-1]  # Переворачиваем тело
            ]
        )  # Добавляем тело

        self._need_enlarge += 2
