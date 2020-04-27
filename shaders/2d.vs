#version 330 core

uniform mat4 u_projection;
uniform mat4 u_view;
uniform mat4 u_model;

uniform vec3 u_color;

layout (location = 0) in vec2 a_position;

out vec2 position;

void main()
{
    gl_Position = u_projection * u_view * u_model * vec4(a_position, 0.0, 1.0);
    position = a_position.xy;
}
