import numpy as np
import glm
import pygame

from pygl import app
from pygl import shader
from pygl import mesh
from pygl import entity


class Entity2(entity.Entity):
    def __init__(self, shader, mesh):
        super(Entity2, self).__init__(shader, mesh)
        self.shader.set_uniform("u_time")
        self.shader.set_uniform("u_aabb")
        self.size = glm.ivec4()

    def draw(self, proj_mat, view_mat):
        self.shader.use_program()
        self.shader.set_float("u_time", pygame.time.get_ticks() / 1000)
        self.shader.set_vec("u_aabb", self.size)
        super(Entity2, self).draw(proj_mat, view_mat)


app.init()

sh = shader.Shader('shaders/2d.vs', 'shaders/2d_params.fs')
sh.use_program()
sh.set_uniform("u_color")
sh.set_vec("u_color", glm.vec3(0.3, 0.7, 1))

msh = mesh.Mesh()
vbo = np.array([(-1, -1), (1, -1), (1, 1), (-1, 1)], dtype=np.float32)
msh.set_attribute(vbo)
ebo = np.array([0, 1, 2, 0, 2, 3], dtype=np.int32)
msh.set_indices(ebo)

# ent = entity.Entity(sh, msh)
ent = Entity2(sh, msh)
ent.size = glm.vec4(-1, -1, 2, 2)
# ent.rotation.x = -glm.quarter_pi()
app.entities.append(ent)






app.run()
