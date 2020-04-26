#version 330 core

uniform vec3 uColor;

void main()
{
  // gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);

  // or gl_FragColor.rgba = vec4(1.0, 0.0, 0.0, 1.0);

  // or gl_FragColor.rgb = vec3(1.0, 0.0, 0.0);
  //    gl_FragColor.a = 1.0;

  gl_FragColor = vec4(uColor, 1.0);    
}
