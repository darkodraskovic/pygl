float rect_fill(vec2 frag_pos, vec2 size, vec2 anchor) {
    frag_pos = step(0 - anchor * size, frag_pos)
        - step(size - anchor * size, frag_pos);
    return frag_pos.x * frag_pos.y;
}

float rect_stroke(vec2 frag_pos, vec2 size, vec2 anchor, float line_width) {
    return rect_fill(frag_pos, size, anchor)
        - rect_fill(frag_pos, size - line_width, anchor);
}
