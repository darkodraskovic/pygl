#version 330 core

uniform float u_alpha = 1.0;
uniform vec3 u_color = vec3(0.3, 0.4, 0.5);

void main()
{
  gl_FragColor = vec4(u_color, u_alpha);    
}
