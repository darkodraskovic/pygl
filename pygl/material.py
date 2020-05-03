import pygame


class Material():
    def __init__(self, shader):
        shader.set_uniform("u_time")
        shader.set_uniform("u_alpha")
        shader.set_uniform("u_projection")
        shader.set_uniform("u_view")
        shader.set_uniform("u_model")
        self.shader = shader
        self.alpha = 1.0

    def update(self, proj_mat, view_mat, model_mat):
        self.shader.use_program()
        self.shader.set_float("u_time", pygame.time.get_ticks() / 1000)
        self.shader.set_float("u_alpha", self.alpha)
        self.shader.set_mat("u_projection", proj_mat)
        self.shader.set_mat("u_view", view_mat)
        self.shader.set_mat("u_model", model_mat)
