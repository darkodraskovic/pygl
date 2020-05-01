import numpy as np

from pygl import app
from pygl import shader
from pygl import mesh
from pygl import entity

app.init()

sh = shader.Shader('2d.vs', '2d_params.fs')

msh = mesh.Mesh()
vbo = np.array([(-1, -1), (1, -1), (1, 1), (-1, 1)], dtype=np.float32)
msh.set_attribute(vbo)
ebo = np.array([0, 1, 2, 0, 2, 3], dtype=np.int32)
msh.set_indices(ebo)

ent = entity.Entity(sh, msh)
app.entities.append(ent)

app.run()
