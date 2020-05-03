import sys
import os
import OpenGL.GL as gl
import glm
import pygame

from pygl import action as act
from pygl import camera as cam


EXIT = 0


size = (1152, 864)
framerate = 60


class App():
    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
        pygame.init()

        # OpenGL
        self.clear_color = (0.5, 0.5, 0.5, 1.0)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 1)
        self.screen = pygame.display.set_mode(
            size, pygame.DOUBLEBUF | pygame.OPENGL)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glCullFace(gl.GL_BACK)
        gl.glFrontFace(gl.GL_CCW)

        self.clock = pygame.time.Clock()

        pygame.mouse.set_visible(0)
        pygame.event.set_grab(True)
        self.bind_keys()

        self.camera = cam.Camera()
        self.camera.position.z = 3
        self.entities = []
        self.alpha_entities = []

    def bind_keys(self):
        # sys
        act.bind_key(pygame.K_ESCAPE, EXIT)

        # camera
        act.bind_key(pygame.K_w, cam.FORWARD)
        act.bind_key(pygame.K_s, cam.BACKWARD)
        act.bind_key(pygame.K_a, cam.LEFT)
        act.bind_key(pygame.K_d, cam.RIGHT)
        act.bind_key(pygame.K_e, cam.UP)
        act.bind_key(pygame.K_q, cam.DOWN)
        act.bind_mbutton(5, cam.ZOOM_IN)
        act.bind_mbutton(4, cam.ZOOM_OUT)

    def handle_input(self, delta_time):
        camera = self.camera
        act.handle_keys()

        # continuous actions
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

        # discrete actions
        for event in pygame.event.get():
            if event.type == act.ACTIONDOWN:
                if event.action == EXIT:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if event.action == cam.ZOOM_OUT:
                    camera.zoom(-1, delta_time)
                elif event.action == cam.ZOOM_IN:
                    camera.zoom(1, delta_time)

        # pygame events
            # if event.type == pygame.MOUSEMOTION:
            #     camera.rotate(pygame.mouse.get_rel(), True)
            if event.type == pygame.QUIT:
                sys.exit()

    def update(self, delta_time):
        for e in self.entities:
            e.update(delta_time)

    def draw(self, delta_time):
        gl.glClearColor(*self.clear_color)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        proj_mat = self.camera.get_projection_matrix(*size)
        view_mat = self.camera.get_view_matrix()

        gl.glEnable(gl.GL_CULL_FACE)
        for e in self.entities:
            e.draw(proj_mat, view_mat)
        gl.glDisable(gl.GL_CULL_FACE)

        self.alpha_entities.sort(
            key=lambda e: glm.length(self.camera.position - e.position),
            reverse=True)
        gl.glEnable(gl.GL_BLEND)
        for e in self.alpha_entities:
            e.draw(proj_mat, view_mat)
        gl.glDisable(gl.GL_BLEND)

        pygame.display.flip()

    def run(self):
        while True:
            delta_time = self.clock.get_time() / 1000

            self.handle_input(delta_time)
            self.update(delta_time)
            self.draw(delta_time)

            self.clock.tick(framerate)
