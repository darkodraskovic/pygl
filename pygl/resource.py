import OpenGL.GL as gl
import pygame


def load_texture(file_name, rect=None):
    surface = pygame.image.load(file_name)
    if rect:
        surface = surface.subsurface(rect)

    data = pygame.image.tostring(surface, "RGBA", 1)
    width = surface.get_width()
    height = surface.get_height()

    texture = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, data)

    return texture, width, height
