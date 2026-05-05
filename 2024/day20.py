#!/usr/bin/env python3
# Written by claude

from collections import deque

with open('input_day20', 'r', encoding='utf-8') as f:
    data = f.read().strip()

grid = data.splitlines()
rows = len(grid)
cols = len(grid[0])

start = end = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (r, c)
        elif grid[r][c] == 'E':
            end = (r, c)

def bfs_dist(src):
    dist = {src: 0}
    queue = deque([src])
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                queue.append((nr, nc))
    return dist

dist_from_start = bfs_dist(start)
dist_from_end = bfs_dist(end)
normal = dist_from_start[end]

# Count cheats that save >= 100 picoseconds
THRESHOLD = 100

def count_cheats(max_cheat_len):
    count = 0
    track_cells = list(dist_from_start.keys())
    for (r1, c1) in track_cells:
        d1 = dist_from_start[(r1, c1)]
        for (r2, c2) in track_cells:
            cheat_len = abs(r2 - r1) + abs(c2 - c1)
            if 2 <= cheat_len <= max_cheat_len:
                d2 = dist_from_end.get((r2, c2))
                if d2 is not None:
                    savings = normal - (d1 + cheat_len + d2)
                    if savings >= THRESHOLD:
                        count += 1
    return count

# Part 1: cheats of length exactly 2
print(count_cheats(2))
# Part 2: cheats of length up to 20
print(count_cheats(20))
