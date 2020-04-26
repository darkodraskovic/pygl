import glm
from pygl import transform

NEAR = 0.1
FAR = 100.0
WORLD_UP = glm.vec3(0, 1, 0)

YAW = -glm.half_pi()
PITCH = 0.0
SPEED = 5.0
SENSITIVITY = 0.5 * 10e-3
ZOOM = glm.quarter_pi()
ZOOM_SPEED = glm.half_pi()
ZOOM_MAX = glm.half_pi()
FORWARD = 1
BACKWARD = 2
LEFT = 3
RIGHT = 4
UP = 5
DOWN = 6


class Camera(transform.Transform):
    def __init__(self, world_up=WORLD_UP, yaw=YAW, pitch=PITCH):
        super(Camera, self).__init__()

        # attributes
        self.right = glm.vec3(1, 0, 0)
        self.up = glm.vec3(0, 1, 0)
        self.front = glm.vec3(0, 0, -1)
        self.world_up = WORLD_UP

        # Euleur angles
        self.rotation.x = pitch
        self.rotation.y = yaw

        # options
        self.speed = SPEED
        self.sensitivity = SENSITIVITY
        self.current_zoom = ZOOM

        self.update_vectors()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.front, self.up)

    def get_projection_matrix(self, scr_width, scr_height):
        return glm.perspective(self.current_zoom, scr_width / scr_height, NEAR, FAR)

    def update_vectors(self):
        front = glm.vec3()
        front.x = glm.cos(self.rotation.y) * glm.cos(self.rotation.x)
        front.y = glm.sin(self.rotation.x)
        front.z = glm.sin(self.rotation.y) * glm.cos(self.rotation.x)
        self.front = glm.normalize(front)
        self.right = glm.normalize(glm.cross(self.front, self.world_up))
        self.up = glm.normalize(glm.cross(self.right, self.front))

    def translate(self, direction, delta_time):
        velocity = self.speed * delta_time
        if (direction == FORWARD):
            self.position += self.front * velocity
        if (direction == BACKWARD):
            self.position -= self.front * velocity
        if (direction == LEFT):
            self.position -= self.right * velocity
        if (direction == RIGHT):
            self.position += self.right * velocity
        if (direction == UP):
            self.position += self.up * velocity
        if (direction == DOWN):
            self.position -= self.up * velocity

    def rotate(self, offset, constrain):
        self.rotation.y += offset[0] * SENSITIVITY
        self.rotation.x -= offset[1] * SENSITIVITY

        if (constrain):
            self.rotation.x = glm.clamp(self.rotation.x, -glm.half_pi(), glm.half_pi())

        self.update_vectors()

    def zoom(self, direction, delta_time):
        self.current_zoom += direction * ZOOM_SPEED * delta_time
        self.current_zoom = glm.clamp(self.current_zoom, 0, ZOOM_MAX)
