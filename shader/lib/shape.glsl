float rect(vec2 pos, vec2 size, vec2 anchor) {
    pos = step(0 - anchor * size, pos) - step(size - anchor * size, pos);
    return pos.x * pos.y;
}
