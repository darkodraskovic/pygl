import re
import OpenGL.GL as gl
import glm


regexp = "\#include\s+(.*)$"


class Shader():
    def __init__(self, vertex_file, fragment_file,
                 dir_name="shader", lib_name="lib"):
        super(Shader, self).__init__()
        vertex_src = Shader.include(vertex_file, dir_name, lib_name)
        fragment_src = Shader.include(fragment_file, dir_name, lib_name)

        self.uniforms = {}
        self.program = gl.glCreateProgram()
        vertex_obj = gl.glCreateShader(gl.GL_VERTEX_SHADER)
        fragment_obj = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
        gl.glShaderSource(vertex_obj, vertex_src)
        gl.glShaderSource(fragment_obj, fragment_src)

        gl.glCompileShader(vertex_obj)
        if not gl.glGetShaderiv(vertex_obj, gl.GL_COMPILE_STATUS):
            error = gl.glGetShaderInfoLog(vertex_obj).decode()
            print(error)
            raise RuntimeError("Vertex shader compilation error")

        gl.glCompileShader(fragment_obj)
        if not gl.glGetShaderiv(fragment_obj, gl.GL_COMPILE_STATUS):
            error = gl.glGetShaderInfoLog(fragment_obj).decode()
            print(error)
            raise RuntimeError("Fragment shader compilation error")

        gl.glAttachShader(self.program, vertex_obj)
        gl.glAttachShader(self.program, fragment_obj)
        gl.glLinkProgram(self.program)
        if not gl.glGetProgramiv(self.program, gl.GL_LINK_STATUS):
            error = gl.glGetProgramInfoLog(self.program)
            print(error)
            raise RuntimeError('Linking error')

        gl.glDetachShader(self.program, vertex_obj)
        gl.glDetachShader(self.program, fragment_obj)

    @staticmethod
    def include(file_name, dir_name, lib_name):
        src = ""
        with open(dir_name + "/" + file_name, 'r') as file:
            for line in file:
                if line.startswith("#include"):
                    m = re.search(regexp, line)
                    line = open(dir_name + "/" + lib_name + "/"
                                + m.group(1) + ".glsl", "r").read()
                src += line
            file.close()
        return src

    def use_program(self):
        gl.glUseProgram(self.program)

    def set_uniform(self, name):
        self.uniforms[name] = gl.glGetUniformLocation(self.program, name)

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
