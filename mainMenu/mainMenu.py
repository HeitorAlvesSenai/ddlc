from loadTexture import load_texture_2d
from mainMenu.ui import draw_quad


import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D


class MainMenu:
    def __init__(self, game):
        self.game = game
        self.init = True
        
        self.mx, self.mv = 0, 0

        self.title = pg.image.load('textures/background01.jpg').convert_alpha()
        
        self.back_ground = load_texture_2d(self.title, GL_REPEAT)
        self.width = game.cw
        self.height = game.ch

    def draw(self):
        self.menu_background()

    def menu_background(self):
        self.dt_sec = self.game.dt_sec
        scroll_speed = self.dt_sec * 0.15
        self.mx += scroll_speed
        self.mv -= scroll_speed
        if self.mx >= 1.0: self.mx -= 1.0
        if self.mv <= -1.0:  self.mv += 1.0
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

        self.draw_quad(self.back_ground, 0, 0, self.width, self.height, self.mx,self.mv)
        glDisable(GL_TEXTURE_2D)
        glEnable(GL_DEPTH_TEST)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        
    def draw_quad(self, tex, x, y, w, h, mx=0, mv=0):
        """Desenha um quad com textura e offset de animação"""
        tex_id, tw, th = tex
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glBegin(GL_QUADS)
        # Ponto 0,0 da textura + offset
        glTexCoord2f(mx, mv)
        glVertex2f(x, y)
        
        # Ponto 1,0 da textura + offset (Horizontal)
        glTexCoord2f(mx + 1, mv)
        glVertex2f(x + w, y)
        
        # Ponto 1,1 da textura + offset (Horizontal e Vertical)
        glTexCoord2f(mx + 1, mv + 1)
        glVertex2f(x + w, y + h)
        
        # Ponto 0,1 da textura + offset (Vertical)
        glTexCoord2f(mx, mv + 1)
        glVertex2f(x, y + h)
        glEnd()