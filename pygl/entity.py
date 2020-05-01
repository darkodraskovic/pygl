import pygame
from pygl import transform


class Entity(transform.Transform):
    def __init__(self, shader, mesh):
        super(Entity, self).__init__()
        shader.set_uniform("u_projection")
        shader.set_uniform("u_view")
        shader.set_uniform("u_model")
        shader.set_uniform("u_time")
        self.shader = shader
        self.mesh = mesh

    def update(self, delta_time):
        pass

    def draw(self, proj_mat, view_mat):
        self.shader.use_program()
        self.shader.set_float("u_time", pygame.time.get_ticks() / 1000)
        self.shader.set_mat("u_projection", proj_mat)
        self.shader.set_mat("u_view", view_mat)
        self.shader.set_mat("u_model", super().get_transform())
        self.mesh.draw()
