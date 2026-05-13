import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

from mainMenu.mainMenu import MainMenu
from mainMenu.icon import Icon
from mainMenu.interface import Interface

class Game:
    def __init__(self):
        pg.init()
        info = pg.display.Info()
        width = info.current_w
        height = info.current_h
        display = (width, height)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL | FULLSCREEN | SCALED)
        self.cw = width
        self.ch = height

        # Ativar profundidade e iluminação
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHT0)

        self.clock = pg.time.Clock()

        # No seu setup inicial
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        self.mainMenu = MainMenu(self)
        self.icon = Icon(self)
        self.interface = Interface(self)

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        self.interface.update()
        self.icon.update()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.mainMenu.draw()
        self.interface.draw()
        self.icon.draw()
        pg.display.flip()

    def run(self):
        while True:
            self.dt = self.clock.tick(67)
            self.dt_sec = self.dt / 1000.0
            self.update()
            self.draw()
            self.checkEvents()

if __name__ == "__main__":
    game = Game()
    game.run()