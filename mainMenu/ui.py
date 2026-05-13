from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D

def draw_quad( tex, x, y, w, h,
              mx=0,mv=1):
    """Desenha um quad com textura"""
    tex_id, tw, th = tex
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glBegin(GL_QUADS)
    glTexCoord2f(mx, mx); glVertex2f(x, y)
    glTexCoord2f(mv, mx); glVertex2f(x+w, y)
    glTexCoord2f(mv, mv); glVertex2f(x+w, y+h)
    glTexCoord2f(mx, mv); glVertex2f(x, y+h)
    glEnd()