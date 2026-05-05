#!/usr/bin/env python3
# Written by claude

import re

with open('input_day13', 'r', encoding='utf-8') as f:
    data = f.read().strip()

machines = []
for block in data.split('\n\n'):
    nums = list(map(int, re.findall(r'\d+', block)))
    ax, ay, bx, by, px, py = nums
    machines.append((ax, ay, bx, by, px, py))

def solve(ax, ay, bx, by, px, py):
    # Solve: a*ax + b*bx = px, a*ay + b*by = py
    det = ax * by - ay * bx
    if det == 0:
        return None
    a_num = px * by - py * bx
    b_num = ax * py - ay * px
    if a_num % det != 0 or b_num % det != 0:
        return None
    a = a_num // det
    b = b_num // det
    if a < 0 or b < 0:
        return None
    return 3 * a + b

# Part 1: up to 100 presses, A costs 3 tokens, B costs 1
total1 = 0
for ax, ay, bx, by, px, py in machines:
    cost = solve(ax, ay, bx, by, px, py)
    if cost is not None:
        total1 += cost
print(total1)

# Part 2: add 10000000000000 to prize positions
OFFSET = 10000000000000
total2 = 0
for ax, ay, bx, by, px, py in machines:
    cost = solve(ax, ay, bx, by, px + OFFSET, py + OFFSET)
    if cost is not None:
        total2 += cost
print(total2)
