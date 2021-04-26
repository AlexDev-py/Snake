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
FONT_COLOR = pg.Color("White")
SNAKE_BODY_COLOR = pg.Color("Green")
SNAKE_HEAD_COLOR = pg.Color("DarkGreen")
APPLE_COLOR = pg.Color("Red")

LOSE_TEXT = pg.font.SysFont(name="Arial", size=40).render(
    "Вы проиграли", True, FONT_COLOR
)
PAUSE_TEXT = pg.font.SysFont(name="Arial", size=40).render("Пауза", True, FONT_COLOR)
TAP_TO_PLAY_TEXT = pg.font.SysFont(name="Calibri", size=20).render(
    "нажмите ПРОБЕЛ чтобы играть", True, FONT_COLOR
)
