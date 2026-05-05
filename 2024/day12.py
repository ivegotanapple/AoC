#!/usr/bin/env python3
# Written by claude

with open('input_day12', 'r', encoding='utf-8') as f:
    data = f.read().strip()

grid = data.splitlines()
rows = len(grid)
cols = len(grid[0])
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[False] * cols for _ in range(rows)]

def flood_fill(sr, sc):
    ch = grid[sr][sc]
    region = []
    stack = [(sr, sc)]
    visited[sr][sc] = True
    while stack:
        r, c = stack.pop()
        region.append((r, c))
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == ch:
                visited[nr][nc] = True
                stack.append((nr, nc))
    return region

def perimeter(region):
    region_set = set(region)
    perim = 0
    for r, c in region:
        for dr, dc in dirs:
            if (r + dr, c + dc) not in region_set:
                perim += 1
    return perim

def count_sides(region):
    region_set = set(region)
    # Count corners = number of sides
    # A cell contributes a corner for each pair of adjacent perpendicular edges
    corners = 0
    for r, c in region:
        # Check all 4 corners of this cell
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            # The two orthogonal neighbors and the diagonal neighbor
            vert = (r + dr, c) in region_set
            horiz = (r, c + dc) in region_set
            diag = (r + dr, c + dc) in region_set
            # Convex corner: neither neighbor is in region
            if not vert and not horiz:
                corners += 1
            # Concave corner: both neighbors in region but not diagonal
            elif vert and horiz and not diag:
                corners += 1
    return corners

total1 = 0
total2 = 0
for r in range(rows):
    for c in range(cols):
        if not visited[r][c]:
            region = flood_fill(r, c)
            area = len(region)
            total1 += area * perimeter(region)
            total2 += area * count_sides(region)

# Part 1: area * perimeter
print(total1)
# Part 2: area * sides (discount fencing)
print(total2)
