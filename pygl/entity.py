from pygl import transform


class Entity(transform.Transform):
    def __init__(self, shader, mesh):
        super(Entity, self).__init__()
        self.shader = shader
        self.shader.set_uniform_location("uProjection")
        self.shader.set_uniform_location("uView")
        self.shader.set_uniform_location("uModel")

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
