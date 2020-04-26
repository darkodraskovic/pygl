import numpy as np
import glm

from pygl import app
from pygl import shader
from pygl import mesh
from pygl import entity

app.init()

sh = shader.Shader('shaders/2d.vs', 'shaders/2d.fs')
sh.use_program()
sh.set_uniform_location("uColor")
sh.set_vec("uColor", glm.vec3(0.3, 0.7, 1))
msh = mesh.Mesh()
vbo = np.array([(-1, -1), (1, -1), (1, 1), (-1, 1)], dtype=np.float32)
msh.set_attribute(vbo)
ebo = np.array([0, 1, 2, 0, 2, 3], dtype=np.int32)
msh.set_indices(ebo)

ent = entity.Entity(sh, msh)
ent.rotation.x = -glm.quarter_pi()

app.entities.append(ent)
# app.camera.position.y = 1
app.camera.update_vectors()

app.run()
