#version 330 core

#define PI 3.14159265359

#include matrix
#include shape


uniform float u_time;
uniform vec4 u_aabb;

uniform vec3 u_color;

in vec3 v_position;

mat3 getScaleMatrix(float scale){
  return mat3(scale,0,0,0,scale,0,0,0,1);
}

vec3 color = vec3(0,0,0);

void main()
{
    vec3 st = v_position;

    float sin_t = sin(u_time);
    float cos_t = cos(u_time);
    float sin_pi = sin_t * PI;
    float cos_pi = cos_t * PI;
    
    st = scale(vec2(.4)) * rotate(u_time) * translate(vec2(.3)) * st;
    color.g += rect(st.xy, vec2(0.3), vec2(0.5));
    
    color.g *= 0.8;
    st = v_position;
    
    gl_FragColor = vec4(color, 1.0);
}
