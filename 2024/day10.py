#!/usr/bin/env python3
# Written by claude

with open('input_day10', 'r', encoding='utf-8') as f:
    data = f.read().strip()

grid = [[int(c) for c in row] for row in data.splitlines()]
rows = len(grid)
cols = len(grid[0])

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs_from(sr, sc):
    reachable_nines = set()
    rating = 0
    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()
        h = grid[r][c]
        if h == 9:
            reachable_nines.add((r, c))
            rating += 1
            continue
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == h + 1:
                stack.append((nr, nc))
    return len(reachable_nines), rating

score1 = 0
score2 = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0:
            nines, paths = bfs_from(r, c)
            score1 += nines
            score2 += paths

# Part 1: sum of reachable 9s per trailhead
print(score1)
# Part 2: sum of distinct trail ratings
print(score2)
