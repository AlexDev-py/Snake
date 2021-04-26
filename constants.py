import pygame as pg

pg.init()

MAX_FPS = 60  # ФПС в игре
PIXEL_SIZE = 14  # Размер одной клетки
PIXELS_COUNT = 35  # Сколько клеток на поле
SPEED = 10  # Сколько клеток, змейка проходит за секунду

DISPLAY_SIZE = PIXEL_SIZE * (PIXELS_COUNT + 4)  # Размер окна
DISPLAY_SIZE = (DISPLAY_SIZE, DISPLAY_SIZE)

FIELD_IMG = r"img\field.png"

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
KEY_MAP = {pg.K_LEFT: LEFT, pg.K_RIGHT: RIGHT, pg.K_UP: UP, pg.K_DOWN: DOWN}

BACKGROUND = pg.Color("Black")
SNAKE_BODY_COLOR = pg.Color("Green")
SNAKE_HEAD_COLOR = pg.Color("DarkGreen")
