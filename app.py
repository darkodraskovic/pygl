import sys
import OpenGL.GL as gl
import pygame

import keyboard as kbd
import camera as cam

clock = pygame.time.Clock()

size = (800, 600)
clear_color = (0.5, 0.5, 0.5, 1.0)

camera = cam.Camera()
entities = []


EXIT = 0


def bind_keys():
    kbd.bind_key(pygame.K_ESCAPE, EXIT)
    kbd.bind_key(pygame.K_w, cam.FORWARD)
    kbd.bind_key(pygame.K_s, cam.BACKWARD)
    kbd.bind_key(pygame.K_a, cam.LEFT)
    kbd.bind_key(pygame.K_d, cam.RIGHT)
    kbd.bind_key(pygame.K_e, cam.UP)
    kbd.bind_key(pygame.K_q, cam.DOWN)


def init():
    pygame.init()
    gl.glEnable(gl.GL_DEPTH_TEST)
    pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)
    bind_keys()
    camera.position.z = 3


def handle_input(delta_time):
    # key pressed
    kbd.handle_keys()

    if kbd.is_pressed(cam.FORWARD):
        camera.translate(cam.FORWARD, delta_time)
    elif kbd.is_pressed(cam.BACKWARD):
        camera.translate(cam.BACKWARD, delta_time)
    if kbd.is_pressed(cam.LEFT):
        camera.translate(cam.LEFT, delta_time)
    elif kbd.is_pressed(cam.RIGHT):
        camera.translate(cam.RIGHT, delta_time)
    if kbd.is_pressed(cam.UP):
        camera.translate(cam.UP, delta_time)
    elif kbd.is_pressed(cam.DOWN):
        camera.translate(cam.DOWN, delta_time)

    # key up/down
    for event in kbd.get():
        if event.type == kbd.KEYDOWN:
            if event.action == EXIT:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update(delta_time):
    for e in entities:
        e.update(delta_time)


def draw(delta_time):
    gl.glClearColor(*clear_color)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    proj_mat = camera.get_projection_matrix(*size)
    view_mat = camera.get_view_matrix()

    for e in entities:
        e.draw(proj_mat, view_mat)


def run():
    global clock

    while True:
        delta_time = clock.get_time() / 1000

        handle_input(delta_time)
        update(delta_time)
        draw(delta_time)

        pygame.display.flip()
        clock.tick(60)
