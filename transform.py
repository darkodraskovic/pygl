import glm


class Transform():
    def __init__(self):
        super(Transform, self).__init__()
        self.position = glm.vec3(0)
        self.rotation = glm.vec3(0)
        self.scale = glm.vec3(1)

    def draw(self):
        transform = glm.mat4(1)
        transform = glm.translate(transform, self.position)
        transform = glm.rotate(transform, self.rotation.x, glm.vec3(1, 0, 0))
        transform = glm.rotate(transform, self.rotation.y, glm.vec3(0, 1, 0))
        transform = glm.rotate(transform, self.rotation.z, glm.vec3(0, 0, 1))
        transform = glm.scale(transform, self.scale)
        return transform
