#!/usr/bin/env python3
# Written by claude

with open('input_day25', 'r', encoding='utf-8') as f:
    data = f.read().strip()

locks = []
keys = []

for block in data.split('\n\n'):
    lines = block.splitlines()
    if lines[0] == '#####':
        # Lock: count # from top down (rows 1-5)
        heights = []
        for c in range(5):
            h = sum(1 for r in range(1, 6) if lines[r][c] == '#')
            heights.append(h)
        locks.append(heights)
    else:
        # Key: count # from bottom up (rows 0-4)
        heights = []
        for c in range(5):
            h = sum(1 for r in range(0, 5) if lines[r][c] == '#')
            heights.append(h)
        keys.append(heights)

# Part 1: count lock/key pairs that fit (no column overlap > 5)
count = 0
for lock in locks:
    for key in keys:
        if all(lock[i] + key[i] <= 5 for i in range(5)):
            count += 1

print(count)
