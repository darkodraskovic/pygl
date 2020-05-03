import numpy as np
import glm
from pygl import app
from pygl import shader
from pygl import material
from pygl import mesh
from pygl import entity

application = app.App()

# shader
# sh = shader.Shader('2d.vs', 'gen_art/03.fs')
sh = shader.Shader('2d.vs', '2d.fs')
mt_red = material.Material(sh)
mt_red.color = glm.vec3(1, 0, 0)

mt_yellow = material.Material(sh)
mt_yellow.color = glm.vec3(1, 1, 0)
mt_yellow.alpha = 0.5
# mesh
msh = mesh.Mesh()
vbo: np.ndarray = np.array([(-1, -1), (1, -1), (1, 1), (-1, 1)], dtype=np.float32)

msh.set_attribute(vbo)
ebo = np.array([0, 1, 2, 0, 2, 3], dtype=np.int32)
msh.set_indices(ebo)

# entity
ent1 = entity.Entity(mt_red, msh)
ent2 = entity.Entity(mt_yellow, msh)

delta = glm.vec3(0.3, 0.3, 0.0)
ent1.position += delta
ent2.position -= delta
ent2.position.z = .01
ent2.rotation.y = 0.2

application.entities.append(ent1)
application.alpha_entities.append(ent2)

application.run()
