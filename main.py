import numpy as np
import glm

import app
import shader
import mesh
import entity

app.init()

sh = shader.Shader('shaders/2d.vs', 'shaders/2d.fs')
sh.use_program()
sh.set_uniform_location("uColor")
sh.set_vec("uColor", glm.vec3(0.3, 0.7, 1))
msh = mesh.Mesh()
data = np.array([(-1, +1), (+1, +1), (-1, -1), (+1, -1)], dtype=np.float32)
msh.set_attribute(data)

ent = entity.Entity(sh, msh)
ent.scale.x = 0.5
ent.scale.y = 0.5
ent.rotation.z = glm.quarter_pi()

app.entities.append(ent)

app.run()
