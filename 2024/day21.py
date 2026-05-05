#!/usr/bin/env python3
# Written by claude

from functools import lru_cache
from itertools import product

with open('input_day21', 'r', encoding='utf-8') as f:
    data = f.read().strip()

codes = data.splitlines()

# Numeric keypad layout
# 7 8 9
# 4 5 6
# 1 2 3
#   0 A
numpad = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2),
}
num_gap = (3, 0)  # gap position

# Directional keypad layout
#   ^ A
# < v >
dirpad = {
                 '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}
dir_gap = (0, 0)  # gap position

def get_moves(fr, fc, tr, tc, gap):
    dr = tr - fr
    dc = tc - fc
    vert = ('v' if dr > 0 else '^') * abs(dr)
    horiz = ('>' if dc > 0 else '<') * abs(dc)
    options = set()
    # Try horizontal first then vertical
    if not (fr == gap[0] and tc == gap[1]):
        options.add(horiz + vert + 'A')
    # Try vertical first then horizontal
    if not (tr == gap[0] and fc == gap[1]):
        options.add(vert + horiz + 'A')
    return options if options else {'A'}

@lru_cache(maxsize=None)
def min_presses(seq, depth):
    if depth == 0:
        return len(seq)
    total = 0
    cur = 'A'
    for ch in seq:
        fr, fc = dirpad[cur]
        tr, tc = dirpad[ch]
        options = get_moves(fr, fc, tr, tc, dir_gap)
        total += min(min_presses(opt, depth - 1) for opt in options)
        cur = ch
    return total

def solve_code(code, depth):
    # Expand numeric keypad presses into directional sequences
    cur = 'A'
    total = 0
    for ch in code:
        fr, fc = numpad[cur]
        tr, tc = numpad[ch]
        options = get_moves(fr, fc, tr, tc, num_gap)
        total += min(min_presses(opt, depth) for opt in options)
        cur = ch
    return total

# Part 1: 2 directional robots
ans1 = sum(solve_code(code, 2) * int(code[:-1]) for code in codes)
print(ans1)

# Part 2: 25 directional robots
ans2 = sum(solve_code(code, 25) * int(code[:-1]) for code in codes)
print(ans2)
