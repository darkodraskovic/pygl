#version 330 core

uniform mat4 uProjection;
uniform mat4 uView;
uniform mat4 uModel;

uniform vec3 uColor;

layout (location = 0) in vec2 aPosition;

void main()
{
    // gl_Position = vec4(aPosition, 0.0, 1.0);

    // or gl_Position.xyzw = vec4(position, 0.0, 1.0);

    // or gl_Position.xy = position;
    //    gl_Position.zw = vec2(0.0, 1.0);

    // or gl_Position.x = position.x;
    //    gl_Position.y = position.y;
    //    gl_Position.z = 0.0;
    //    gl_Position.w = 1.0;

    gl_Position = uProjection * uView * uModel * vec4(aPosition, 0.0, 1.0);
}
