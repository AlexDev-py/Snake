from typing import List

import pygame as pg
import pygame.display

import constants as const
from field import Field, Pixel, random_cords
from snake import Snake

pg.init()

screen = pg.display.set_mode(const.DISPLAY_SIZE)
pg.display.set_caption("Mega Snake")
clock = pg.time.Clock()


class Game:
    def __init__(self):
        self.game = True  # Флаг, показывающий идет ли игра
        self.pause = False
        self.lose = False
        self.field = Field()
        self.snake = Snake()

        # Действия, которые необходимо выполнить далее
        self._events_buffer: List[pg.event.Event] = []

        self.generate_apple()  # Создаём первое яблоко

    def generate_apple(self):
        """
        Генерируем яблоко в свободной клетке
        """

        apple = random_cords()
        # Занятые клетки
        not_available_pixels = [
            *[pixel.cords for pixel in self.field.apples],
            *[pixel.cords for pixel in self.snake],
        ]
        while apple in not_available_pixels:
            apple = random_cords()
        self.field.apples.append(Pixel(*apple, const.APPLE_COLOR))

    def check_collision(self):
        head = self.snake[0].cords

        # Столкновение с краем
        if not (0 <= head[0] <= 34) or not (0 <= head[1] <= 34):
            self.lose = True

        # Ест яблоко
        apples = [apple.cords for apple in self.field.apples]
        if head in apples:
            del self.field.apples[apples.index(head)]  # Удаляем съеденное яблоко
            self.generate_apple()  # Создаём новое яблоко
            self.snake.eat()

        # Столкновение с хвостом
        body = [pixel.cords for pixel in self.snake[1:]]
        if head in body:
            self.lose = True

    def restart(self):
        """ Перезапускаем игру """

        self.snake = Snake()
        self.field = Field()
        self.generate_apple()
        self.lose = False
        self.pause = False

    def handle_event(self, event: pg.event.Event, _event_index: int = None):
        """
        Обрабатываем событие.
        :param event: Событие.
        :param _event_index: Индекс события в буфере.
        """

        if event.type == pg.QUIT:  # Нажали на крестик
            self.game = False

        elif event.type == pg.KEYDOWN:  # Нажали клавишу
            if event.key in const.KEY_MAP:
                if self.snake.can_change_direction:
                    self.snake.change_direction(const.KEY_MAP[event.key])
                    if _event_index is not None:
                        del self._events_buffer[_event_index]
                else:
                    # Добавляем событие в буфер
                    if _event_index is None:
                        self._events_buffer.append(event)

            elif event.key == pg.K_SPACE:
                self.pause = not self.pause
                if self.lose:
                    self.restart()

    def draw(self):
        """ Отображаем игру """

        screen.fill(const.BACKGROUND)  # Создаём фон

        if not self.pause and not self.lose:
            self.snake.move()
        self.snake.draw(screen)

        for apple in self.field.apples:
            apple.draw(screen)

        self.field.draw_grid(screen)

        if self.lose:
            center = const.DISPLAY_SIZE[0] // 2  # Центр экрана
            screen.blit(
                const.LOSE_TEXT,
                (
                    center - const.LOSE_TEXT.get_width() // 2,
                    center - const.LOSE_TEXT.get_height(),
                ),
            )
            screen.blit(
                const.TAP_TO_PLAY_TEXT,
                (
                    center - const.TAP_TO_PLAY_TEXT.get_width() // 2,
                    center + const.LOSE_TEXT.get_height() // 2,
                ),
            )
        elif self.pause:
            center = const.DISPLAY_SIZE[0] // 2  # Центр экрана
            screen.blit(
                const.PAUSE_TEXT,
                (
                    center - const.PAUSE_TEXT.get_width() // 2,
                    center - const.PAUSE_TEXT.get_height(),
                ),
            )
            screen.blit(
                const.TAP_TO_PLAY_TEXT,
                (
                    center - const.TAP_TO_PLAY_TEXT.get_width() // 2,
                    center + const.PAUSE_TEXT.get_height() // 2,
                ),
            )

    def mainloop(self):
        """ Основной цикл программы """

        while self.game:
            clock.tick(const.MAX_FPS)

            self.check_collision()
            self.draw()
            pygame.display.flip()

            for i, event in enumerate(self._events_buffer):
                self.handle_event(event, _event_index=i)
            for event in pg.event.get():
                self.handle_event(event)


if __name__ == "__main__":
    game = Game()
    game.mainloop()
