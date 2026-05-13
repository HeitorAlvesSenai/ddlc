from OpenGL.GL import *
from pygame import image

def load_texture_2d(surface, parameter=GL_CLAMP_TO_EDGE):
    """Converte pygame.Surface em textura OpenGL e retorna o ID"""
    tex_data = image.tostring(surface, "RGBA", True)
    width, height = surface.get_size()
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    if parameter == GL_CLAMP_TO_EDGE:
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, parameter)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, parameter)
    elif parameter == GL_REPEAT:
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, parameter)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, parameter)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                    GL_RGBA, GL_UNSIGNED_BYTE, tex_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return tex_id, width, height