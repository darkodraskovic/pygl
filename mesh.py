import OpenGL.GL as gl
import ctypes


class Mesh():
    def __init__(self):
        super(Mesh, self).__init__()
        self.vao = gl.glGenVertexArrays(1)
        self.vbos = []
        self.num_vertices = 0
        self.mode = gl.GL_TRIANGLE_STRIP

    def set_attribute(self, data):
        self.num_vertices = data.shape[0]
        gl.glBindVertexArray(self.vao)

        attr_buffer = gl.glGenBuffers(1)
        self.vbos.append(attr_buffer)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, attr_buffer)

        stride = data.strides[0]
        offset = ctypes.c_void_p(0)
        loc = len(self.vbos) - 1
        gl.glEnableVertexAttribArray(loc)
        gl.glVertexAttribPointer(loc, data.shape[1], gl.GL_FLOAT, False, stride, offset)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, data.nbytes, data, gl.GL_DYNAMIC_DRAW)

        gl.glBindVertexArray(self.vao)

    def draw(self):
        gl.glBindVertexArray(self.vao)
        gl.glDrawArrays(self.mode, 0, self.num_vertices)
        gl.glBindVertexArray(0)
