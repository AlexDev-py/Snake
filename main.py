from typing import List

import pygame as pg
import pygame.display

import constants as const
from field import Field
from snake import Snake

pg.init()

screen = pg.display.set_mode(const.DISPLAY_SIZE)
pg.display.set_caption("Mega Snake")
clock = pg.time.Clock()


class Game:
    def __init__(self):
        self.game = True  # Флаг, показывающий идет ли игра
        self.field = Field()
        self.snake = Snake()

        # Действия, которые необходимо выполнить далее
        self._events_buffer: List[pg.event.Event] = []

    def stop_game(self):
        """ Выключает игру """

        self.game = False

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

    def draw(self):
        """ Отображаем игру """

        screen.fill(const.BACKGROUND)  # Создаём фон

        self.snake.move()
        self.snake.draw(screen)

        self.field.draw_grid(screen)

    def mainloop(self):
        """ Основной цикл программы """

        while self.game:
            clock.tick(const.MAX_FPS)

            self.draw()
            pygame.display.flip()

            for i, event in enumerate(self._events_buffer):
                self.handle_event(event, _event_index=i)
            for event in pg.event.get():
                self.handle_event(event)


if __name__ == "__main__":
    game = Game()
    game.mainloop()
