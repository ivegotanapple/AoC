#!/usr/bin/env python3
# Written by claude

from collections import deque

with open('input_day18', 'r', encoding='utf-8') as f:
    data = f.read().strip()

bytes_list = [tuple(map(int, line.split(','))) for line in data.splitlines()]

SIZE = 71  # 0 to 70

def bfs(blocked):
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}
    while queue:
        steps, r, c = queue.popleft()
        if r == SIZE - 1 and c == SIZE - 1:
            return steps
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < SIZE and 0 <= nc < SIZE and (nr, nc) not in visited and (nc, nr) not in blocked:
                visited.add((nr, nc))
                queue.append((steps + 1, nr, nc))
    return None

# Part 1: after first 1024 bytes
blocked = set(bytes_list[:1024])
print(bfs(blocked))

# Part 2: find first byte that blocks all paths (binary search)
lo, hi = 1024, len(bytes_list) - 1
while lo < hi:
    mid = (lo + hi) // 2
    blocked = set(bytes_list[:mid + 1])
    if bfs(blocked) is None:
        hi = mid
    else:
        lo = mid + 1

bx, by = bytes_list[lo]
print(f'{bx},{by}')
