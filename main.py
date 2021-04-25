import pygame as pg
import pygame.display

import gamerules as gr
from field import Field, Pixel
from snake import Snake

pg.init()

screen = pg.display.set_mode(gr.DISPLAY_SIZE)
pg.display.set_caption("Mega Snake")
font = pg.font.SysFont("Calibri", 20)
clock = pg.time.Clock()


class Game:
    def __init__(self):
        self.game = True  # Флаг, показывающий идет ли игра
        self.field = Field()
        self.snake = Snake()

    def stop_game(self):
        """ Выключает игру """
        self.game = False

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.QUIT:
            self.game = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.snake.direction = "top"
            if event.key == pg.K_DOWN:
                self.snake.direction = "down"
            if event.key == pg.K_RIGHT:
                self.snake.direction = "right"
            if event.key == pg.K_LEFT:
                self.snake.direction = "left"

    def draw(self):
        screen.fill(pg.Color("Black"))

        self.snake.move()
        self.snake.draw(screen)

        self.field.draw_grid(screen)

    def mainloop(self):
        """ Основной цикл программы """

        while self.game:
            clock.tick(gr.MAX_FPS)

            self.draw()
            pygame.display.flip()

            for event in pg.event.get():
                self.handle_event(event)


if __name__ == "__main__":
    game = Game()
    game.mainloop()
