#!/usr/bin/env python3
# Written by claude

with open('input_day8', 'r', encoding='utf-8') as f:
    data = f.read().strip()

grid = data.splitlines()
rows = len(grid)
cols = len(grid[0])

from collections import defaultdict

antennas = defaultdict(list)
for r in range(rows):
    for c in range(cols):
        ch = grid[r][c]
        if ch != '.':
            antennas[ch].append((r, c))

# Part 1: antinodes at 2:1 distance ratio from each antenna pair
antinodes1 = set()
for freq, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i == j:
                continue
            r1, c1 = positions[i]
            r2, c2 = positions[j]
            dr = r2 - r1
            dc = c2 - c1
            # antinode is at positions[i] - (r2-r1, c2-c1)
            ar, ac = r1 - dr, c1 - dc
            if 0 <= ar < rows and 0 <= ac < cols:
                antinodes1.add((ar, ac))

print(len(antinodes1))

# Part 2: all harmonic antinodes along the line
antinodes2 = set()
for freq, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            r1, c1 = positions[i]
            r2, c2 = positions[j]
            dr = r2 - r1
            dc = c2 - c1
            # walk in both directions from r1,c1
            for direction in (1, -1):
                r, c = r1, c1
                while 0 <= r < rows and 0 <= c < cols:
                    antinodes2.add((r, c))
                    r += direction * dr
                    c += direction * dc

print(len(antinodes2))
