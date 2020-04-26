import OpenGL.GL as gl
import glm


class Shader():
    def __init__(self, vertex_file, fragment_file):
        super(Shader, self).__init__()

        self.uniforms = {}

        with open(vertex_file, 'r') as file:
            self.vertex_src = file.read()
        with open(fragment_file, 'r') as file:
            self.fragment_src = file.read()

        self.program = gl.glCreateProgram()
        self.vertex_obj = gl.glCreateShader(gl.GL_VERTEX_SHADER)
        self.fragment_obj = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
        gl.glShaderSource(self.vertex_obj, self.vertex_src)
        gl.glShaderSource(self.fragment_obj, self.fragment_src)

        gl.glCompileShader(self.vertex_obj)
        if not gl.glGetShaderiv(self.vertex_obj, gl.GL_COMPILE_STATUS):
            error = gl.glGetShaderInfoLog(self.vertex_obj).decode()
            print(error)
            raise RuntimeError("Vertex shader compilation error")

        gl.glCompileShader(self.fragment_obj)
        if not gl.glGetShaderiv(self.fragment_obj, gl.GL_COMPILE_STATUS):
            error = gl.glGetShaderInfoLog(self.fragment_obj).decode()
            print(error)
            raise RuntimeError("Fragment shader compilation error")

        gl.glAttachShader(self.program, self.vertex_obj)
        gl.glAttachShader(self.program, self.fragment_obj)
        gl.glLinkProgram(self.program)
        if not gl.glGetProgramiv(self.program, gl.GL_LINK_STATUS):
            error = gl.glGetProgramInfoLog(self.program)
            print(error)
            raise RuntimeError('Linking error')

        gl.glDetachShader(self.program, self.vertex_obj)
        gl.glDetachShader(self.program, self.fragment_obj)

    def use_program(self):
        gl.glUseProgram(self.program)

    def get_attrib_location(self, name):
        return gl.glGetAttribLocation(self.program, name)

    def set_uniform_location(self, name):
        self.uniforms[name] = gl.glGetUniformLocation(self.program, name)

    def get_uniform_location(self, name):
        return gl.glGetUniformLocation(self.program, name)

    def set_float(self, name, n):
        gl.glUniform1f(self.uniforms[name], n)

    def set_vec(self, name, vec):
        op = gl.glUniform2fv
        if len(vec) == 3:
            op = gl.glUniform3fv
        elif len(vec) == 4:
            op = gl.glUniform4fv
        op(self.uniforms[name], 1, glm.value_ptr(vec))

    def set_mat(self, name, mat):
        op = gl.glUniformMatrix2fv
        if mat.length() == 3:
            op = gl.glUniformMatrix3fv
        elif mat.length() == 4:
            op = gl.glUniformMatrix4fv
        op(self.uniforms[name], 1, False, glm.value_ptr(mat))
