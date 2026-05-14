from loadTexture import load_texture_2d
from mainMenu.ui import draw_quad
from math import sin


import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D


class Persons:
    def __init__(self, game):
        self.game = game
        self.width = game.cw
        self.height = game.ch
        self.x = self.height
        self.y = self.height
        self.final_point = self.height - self.height
        self.init = True

        self.title = pg.image.load('textures/Monika_DDLC.png').convert_alpha()
        self.back_ground = load_texture_2d(self.title)

        self.start_tick = pg.time.get_ticks()
        self.elapsed_seconds = 0
        self.timer = 0
        
    def update(self):
        # Incrementa o timer (ajuste o 2.0 para mudar a velocidade)
        self.timer += self.game.dt_sec * 2.0 
        
        # Calcula o fator de escala (oscila entre 0.9 e 1.1)
        self.escala = 1.0 + 0.1 * sin(self.timer)
        if self.elapsed_seconds > 1:
            if self.y > self.final_point:
                self.y -= self.game.dt_sec * 500
                if self.y < self.final_point:
                    self.y = self.final_point
        else:self.elapsed_seconds = (pg.time.get_ticks() - self.start_tick) / 1000
            
        pass

    def draw(self):
        self.menu_background()

    def menu_background(self):
        largura_animada = self.height * self.escala
        altura_animada = self.height * self.escala
        offset_centro = (largura_animada - self.height) / 2
        pos_x = self.x - offset_centro
        pos_y = 0 - offset_centro
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
        self.draw_quad(
            self.back_ground,
            pos_x,#(self.height // 1.6),
            pos_y,#self.y,
            largura_animada,#self.height // 2.5,
            altura_animada#self.height // 2.5
            )
        glDisable(GL_TEXTURE_2D)
        glEnable(GL_DEPTH_TEST)
        glColor4f(1.0, 1.0, 1.0, 1.0)
    
    def draw_quad(self, tex, x, y, w, h,
              mx=0,mv=1):
        """Desenha um quad com textura"""
        w *= 0.004
        h *= 0.004
        tex_id, tw, th = tex
        tw *= w
        th *= h
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glBegin(GL_QUADS)
        glTexCoord2f(mx, mx); glVertex2f(x, y)
        glTexCoord2f(mv, mx); glVertex2f(x+tw, y)
        glTexCoord2f(mv, mv); glVertex2f(x+tw, y+th)
        glTexCoord2f(mx, mv); glVertex2f(x, y+th)
        glEnd()