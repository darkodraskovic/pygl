#version 330 core

#define PI 3.14159265359

#include matrix
#include shape

uniform float u_time;

in vec3 v_position;

vec3 color = vec3(0,0,0);

void main()
{
    vec3 st = v_position;

    // float sin_t = sin(u_time);
    // float cos_t = cos(u_time);
    // float sin_pi = sin_t * PI;
    // float cos_pi = cos_t * PI;
    
    st = scale(vec2(.4)) * rotate(u_time) * translate(vec2(.3)) * st;
    color.g += rect_fill(st.xy, vec2(0.3), vec2(0.5));
    
    color.g *= 0.8;
    st = v_position;
    
    gl_FragColor = vec4(color, 1.0);
}
