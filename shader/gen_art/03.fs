#version 330 core

#include matrix
#include shape
#include util

uniform float u_time;

in vec3 v_position;

vec3 color = vec3(0.2,0.3,0.33);

void main()
{
    vec3 st = v_position;

    float x_pos = 0.5;
    float y_pos = 0.25;
    float r_size = 0.1;
    float r_anchor = 0.5;
    float line_width = 0.03;
    
    for (int i = 0; i < 4; i++) {
        int sign_x = alter_sign(i, 2);
        int sign_y = alter_sign(i, 1);

        float x = x_pos * sign_x;
        float y = y_pos * sign_y;

        st = translate(vec2(x, y)) * st;
        // color.r += rect_fill(st.xy, vec2(r_size - line_width), vec2(r_anchor));
        color.g += rect_stroke(st.xy, vec2(r_size), vec2(r_anchor), line_width);
        st = v_position;

        st = translate(vec2(y, x)) * st;
        color.r += rect_fill(st.xy, vec2(r_size - line_width), vec2(r_anchor));
        // color.g += rect_stroke(st.xy, vec2(r_size), vec2(r_anchor), line_width);
        st = v_position;
    }
    
    gl_FragColor = vec4(color, 1.0);
}
