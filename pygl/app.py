import sys
import os
import OpenGL.GL as gl
import pygame

from pygl import action as act
from pygl import camera as cam


clock = pygame.time.Clock()
framerate = 60

position = (0, 0)
size = (1152, 720)
clear_color = (0.5, 0.5, 0.5, 1.0)

camera = cam.Camera()
entities = []


EXIT = 0


def bind_keys():
    act.bind_key(pygame.K_ESCAPE, EXIT)
    act.bind_key(pygame.K_w, cam.FORWARD)
    act.bind_key(pygame.K_s, cam.BACKWARD)
    act.bind_key(pygame.K_a, cam.LEFT)
    act.bind_key(pygame.K_d, cam.RIGHT)
    act.bind_key(pygame.K_e, cam.UP)
    act.bind_key(pygame.K_q, cam.DOWN)


def init():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % position
    pygame.init()
    gl.glEnable(gl.GL_DEPTH_TEST)
    pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)
    bind_keys()
    camera.position.z = 3


def handle_input(delta_time):
    act.handle_keys()

    if act.is_pressed(cam.FORWARD):
        camera.translate(cam.FORWARD, delta_time)
    elif act.is_pressed(cam.BACKWARD):
        camera.translate(cam.BACKWARD, delta_time)
    if act.is_pressed(cam.LEFT):
        camera.translate(cam.LEFT, delta_time)
    elif act.is_pressed(cam.RIGHT):
        camera.translate(cam.RIGHT, delta_time)
    if act.is_pressed(cam.UP):
        camera.translate(cam.UP, delta_time)
    elif act.is_pressed(cam.DOWN):
        camera.translate(cam.DOWN, delta_time)

    for event in pygame.event.get():
        if event.type == act.ACTIONDOWN:
            if event.action == EXIT:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                camera.zoom(-1, delta_time)
            elif event.button == 5:
                camera.zoom(1, delta_time)
        if event.type == pygame.MOUSEMOTION:
            camera.rotate(pygame.mouse.get_rel(), True)
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

    pygame.display.flip()


def run():
    global clock

    while True:
        delta_time = clock.get_time() / 1000

        handle_input(delta_time)
        update(delta_time)
        draw(delta_time)

        clock.tick(framerate)
