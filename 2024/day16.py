#!/usr/bin/env python3
# Written by claude

import heapq

with open('input_day16', 'r', encoding='utf-8') as f:
    data = f.read().strip()

grid = data.splitlines()
rows = len(grid)
cols = len(grid[0])

# Directions: 0=East, 1=South, 2=West, 3=North
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

start_r = start_c = end_r = end_c = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start_r, start_c = r, c
        elif grid[r][c] == 'E':
            end_r, end_c = r, c

# Dijkstra: state = (cost, r, c, direction)
INF = float('inf')
dist = [[[INF] * 4 for _ in range(cols)] for _ in range(rows)]
dist[start_r][start_c][0] = 0  # facing East initially

pq = [(0, start_r, start_c, 0)]

while pq:
    cost, r, c, d = heapq.heappop(pq)
    if cost > dist[r][c][d]:
        continue
    # Move forward
    dr, dc = DIR[d]
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
        new_cost = cost + 1
        if new_cost < dist[nr][nc][d]:
            dist[nr][nc][d] = new_cost
            heapq.heappush(pq, (new_cost, nr, nc, d))
    # Turn left or right (no movement)
    for nd in [(d - 1) % 4, (d + 1) % 4]:
        new_cost = cost + 1000
        if new_cost < dist[r][c][nd]:
            dist[r][c][nd] = new_cost
            heapq.heappush(pq, (new_cost, r, c, nd))

best = min(dist[end_r][end_c])
print(best)

# Part 2: count tiles on all optimal paths (backward BFS from end)
# Find all states that are on an optimal path
on_best = [[[False] * 4 for _ in range(cols)] for _ in range(rows)]

# Backward Dijkstra: from end in all directions
dist_back = [[[INF] * 4 for _ in range(cols)] for _ in range(rows)]
pq2 = []
for d in range(4):
    if dist[end_r][end_c][d] == best:
        dist_back[end_r][end_c][d] = 0
        heapq.heappush(pq2, (0, end_r, end_c, d))

while pq2:
    cost, r, c, d = heapq.heappop(pq2)
    if cost > dist_back[r][c][d]:
        continue
    # Reverse move: came from behind
    dr, dc = DIR[d]
    pr, pc = r - dr, c - dc
    if 0 <= pr < rows and 0 <= pc < cols and grid[pr][pc] != '#':
        new_cost = cost + 1
        if new_cost < dist_back[pr][pc][d]:
            dist_back[pr][pc][d] = new_cost
            heapq.heappush(pq2, (new_cost, pr, pc, d))
    # Reverse turn
    for nd in [(d - 1) % 4, (d + 1) % 4]:
        new_cost = cost + 1000
        if new_cost < dist_back[r][c][nd]:
            dist_back[r][c][nd] = new_cost
            heapq.heappush(pq2, (new_cost, r, c, nd))

# A tile is on a best path if dist[r][c][d] + dist_back[r][c][d] == best for some d
best_tiles = set()
for r in range(rows):
    for c in range(cols):
        for d in range(4):
            if dist[r][c][d] + dist_back[r][c][d] == best:
                best_tiles.add((r, c))

print(len(best_tiles))
