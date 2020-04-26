from pygl import transform


class Entity(transform.Transform):
    def __init__(self, shader, mesh):
        super(Entity, self).__init__()
        shader.set_uniform("uProjection")
        shader.set_uniform("uView")
        shader.set_uniform("uModel")
        self.shader = shader
        self.mesh = mesh

    def update(self, delta_time):
        pass

    def draw(self, proj_mat, view_mat):
        model_mat = super().draw()
        self.shader.use_program()
        self.shader.set_mat("uProjection", proj_mat)
        self.shader.set_mat("uView", view_mat)
        self.shader.set_mat("uModel", model_mat)
        self.mesh.draw()
