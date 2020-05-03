from pygl import transform


class Entity(transform.Transform):
    def __init__(self, material, mesh):
        super(Entity, self).__init__()
        self.material = material
        self.mesh = mesh

    def update(self, delta_time):
        pass

    def draw(self, proj_mat, view_mat):
        model_mat = super().get_transform()
        self.material.update(proj_mat, view_mat, model_mat)
        self.mesh.draw()
