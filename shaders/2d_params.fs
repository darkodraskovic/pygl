#version 330 core

#define PI 3.14159265359

uniform float u_time;
uniform vec4 u_aabb;

uniform vec3 u_color;

in vec2 position;

vec3 color = vec3(0,0,0);

mat3 translate(float x, float y) {
    return mat3(1.0, 0.0, 0.0,
                0.0, 1.0, 0.0,
                -x, -y, 1.0);
}

mat3 rotate(float angle) {
    return mat3(cos(angle), -sin(angle), 0.0,
                sin(angle), cos(angle), 0.0,
                0.0, 0.0, 1.0);
}

mat3 scale(float x, float y){
    return mat3(1/x, 0.0, 0.0,
                0.0, 1/y, 0.0,
                0.0, 0.0, 1.0);
}

float rectangle(vec2 pos, vec2 size, vec2 offset) {
    pos = step(0 - offset, pos) - step(size - offset, pos);
    return pos.x * pos.y;
}

void main()
{
    vec3 st = vec3((position.xy - u_aabb.xy) / u_aabb.zw, 1.0);
    vec3 prev_st = st;
    
    float sin_t = sin(u_time);
    float cos_t = cos(u_time);
    float sin_pi = sin_t * PI;
    float cos_pi = cos_t * PI;
    
    prev_st = st;
    // st = scale(0.4,0.2) * rotate(u_time) * translate(0.3, 0.5) * st;
    
    // st = scale(0.4,0.2) * rotate(0) * translate(0.3, 0.5) * st;
    st = scale(0.4,0.2) * rotate(PI/7) * translate(0.3, 0.5) * st;
    color.g += rectangle(st.xy, vec2(0.3,0.2), vec2(0));
    
    color.g *= 0.8;
    st = prev_st;
    
    gl_FragColor = vec4(color, 1.0);
}
