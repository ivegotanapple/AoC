#!/usr/bin/env python3
# Written by claude

import re
from math import prod

with open('input_day14', 'r', encoding='utf-8') as f:
    data = f.read().strip()

robots = []
for line in data.splitlines():
    nums = list(map(int, re.findall(r'-?\d+', line)))
    px, py, vx, vy = nums
    robots.append((px, py, vx, vy))

WIDTH = 101
HEIGHT = 103

# Part 1: simulate 100 seconds, count robots per quadrant
positions = []
for px, py, vx, vy in robots:
    fx = (px + vx * 100) % WIDTH
    fy = (py + vy * 100) % HEIGHT
    positions.append((fx, fy))

mid_x = WIDTH // 2
mid_y = HEIGHT // 2
quadrants = [0, 0, 0, 0]
for x, y in positions:
    if x == mid_x or y == mid_y:
        continue
    q = (0 if x < mid_x else 1) + (0 if y < mid_y else 2)
    quadrants[q] += 1

print(prod(quadrants))

# Part 2: find when robots form Christmas tree (minimal bounding variance)
# The tree appears when robots cluster together - find minimum variance second
import statistics

min_var = float('inf')
best_t = 0
# Only need to check up to WIDTH*HEIGHT seconds (period)
for t in range(WIDTH * HEIGHT):
    xs = [(px + vx * t) % WIDTH for px, py, vx, vy in robots]
    ys = [(py + vy * t) % HEIGHT for px, py, vx, vy in robots]
    var = statistics.variance(xs) + statistics.variance(ys)
    if var < min_var:
        min_var = var
        best_t = t

print(best_t)
