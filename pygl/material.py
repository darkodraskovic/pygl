import pygame
import glm


class Material():
    def __init__(self, shader):
        shader.set_uniform("u_time")
        shader.set_uniform("u_alpha")
        shader.set_uniform("u_projection")
        shader.set_uniform("u_view")
        shader.set_uniform("u_model")
        shader.set_uniform("u_color")
        self.shader = shader
        self.alpha = 1.0
        self.color = glm.vec3(1, 1, 1)

    def update(self, proj_mat, view_mat, model_mat):
        self.shader.use_program()
        self.shader.set_float("u_time", pygame.time.get_ticks() / 1000)
        self.shader.set_vec("u_color", self.color)
        self.shader.set_float("u_alpha", self.alpha)
        self.shader.set_mat("u_projection", proj_mat)
        self.shader.set_mat("u_view", view_mat)
        self.shader.set_mat("u_model", model_mat)
