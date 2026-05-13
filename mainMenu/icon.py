from loadTexture import load_texture_2d
from mainMenu.ui import draw_quad


import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D


class Icon:
    def __init__(self, game):
        self.game = game
        self.width = game.cw
        self.height = game.ch
        self.y = self.height
        self.final_point = self.height - (self.height // 2.5)
        self.init = True

        self.title = pg.image.load('textures/iconddlc.jpg').convert_alpha()
        self.back_ground = load_texture_2d(self.title)
        
    def update(self):
        if self.y > self.final_point:
            self.y -= self.game.dt_sec * 250
            if self.y < self.final_point:
                self.y = self.final_point
            
        pass
    
    def draw(self):
        self.menu_background()

    def menu_background(self):
        glDisable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, self.width, 0, self.height)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        draw_quad(self.back_ground, (self.height // 4), self.y, self.height // 2.5, self.height // 2.5)
        glDisable(GL_TEXTURE_2D)
        glEnable(GL_DEPTH_TEST)
        glColor4f(1.0, 1.0, 1.0, 1.0)