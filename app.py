import sys
import OpenGL.GL as gl
import pygame

clock = pygame.time.Clock()
delta_time = 0
clear_color = (0.5, 0.5, 0.5, 1.0)
entities = []


def init(width=800, height=600):
    pygame.init()
    gl.glEnable(gl.GL_DEPTH_TEST)
    pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)


def run():
    global clock
    global delta_time
    global entities

    while True:
        gl.glClearColor(*clear_color)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        delta_time = clock.get_time() / 1000
        for e in entities:
            e.update(delta_time)

        for e in entities:
            e.draw()

        pygame.display.flip()
        clock.tick(60)
