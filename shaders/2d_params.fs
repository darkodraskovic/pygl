#version 330 core

uniform float u_time;
uniform vec4 u_aabb;

uniform vec3 u_color;

in vec2 position;

vec3 color = vec3(0,0,0);

void main()
{
    vec2 norm_pos = (position.xy - u_aabb.xy) / u_aabb.zw;
    
    // color = u_color;
    // color = u_color * abs(sin(u_time));
    
    // color = mix(vec3(1,0,0), vec3(0,0,1), norm_pos.y);
    
    // color = vec3(norm_pos, 0.0);
    // color = vec3(step(vec2(0.75, 0.6), norm_pos), 0.0);
    // color = vec3(smoothstep(vec2(0.75, 0.6), vec2(0.8, 0.65), norm_pos), 0.0);

    vec2 center = vec2(abs(sin(u_time)), 0.5) - 0.2;
    vec2 v_diff = norm_pos - center;
    color.rg = 1.0 - step(vec2(0.2,0.2), v_diff);
    
    gl_FragColor = vec4(color, 1.0);
}
