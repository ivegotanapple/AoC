#!/usr/bin/env python3
# Written by claude

with open('input_day15', 'r', encoding='utf-8') as f:
    data = f.read()

map_part, moves_part = data.split('\n\n')
moves = moves_part.replace('\n', '')

# Part 1: normal warehouse
grid = [list(row) for row in map_part.splitlines()]
rows = len(grid)
cols = len(grid[0])

# Find robot
robot_r, robot_c = 0, 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            robot_r, robot_c = r, c
            grid[r][c] = '.'

dir_map = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def try_push(grid, r, c, dr, dc):
    # Returns True if move is possible, and modifies grid
    nr, nc = r + dr, c + dc
    if grid[nr][nc] == '#':
        return False
    if grid[nr][nc] == '.':
        grid[nr][nc] = grid[r][c]
        grid[r][c] = '.'
        return True
    if grid[nr][nc] == 'O':
        if try_push(grid, nr, nc, dr, dc):
            grid[nr][nc] = grid[r][c]
            grid[r][c] = '.'
            return True
    return False

for move in moves:
    dr, dc = dir_map[move]
    nr, nc = robot_r + dr, robot_c + dc
    if grid[nr][nc] == '#':
        continue
    if grid[nr][nc] == '.':
        robot_r, robot_c = nr, nc
    elif grid[nr][nc] == 'O':
        if try_push(grid, nr, nc, dr, dc):
            robot_r, robot_c = nr, nc

gps1 = sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == 'O')
print(gps1)

# Part 2: double-wide warehouse
wide_map = (map_part.replace('#', '##').replace('O', '[]')
            .replace('.', '..').replace('@', '@.'))
grid2 = [list(row) for row in wide_map.splitlines()]
rows2 = len(grid2)
cols2 = len(grid2[0])

robot_r, robot_c = 0, 0
for r in range(rows2):
    for c in range(cols2):
        if grid2[r][c] == '@':
            robot_r, robot_c = r, c
            grid2[r][c] = '.'

def can_push_wide(grid, r, c, dr, dc):
    nr, nc = r + dr, c + dc
    cell = grid[nr][nc]
    if cell == '#':
        return False
    if cell == '.':
        return True
    if dc != 0:  # horizontal - single chain
        return can_push_wide(grid, nr, nc, dr, dc)
    # vertical with wide boxes
    if cell == '[':
        return can_push_wide(grid, nr, nc, dr, dc) and can_push_wide(grid, nr, nc + 1, dr, dc)
    if cell == ']':
        return can_push_wide(grid, nr, nc, dr, dc) and can_push_wide(grid, nr, nc - 1, dr, dc)
    return False

def do_push_wide(grid, r, c, dr, dc):
    nr, nc = r + dr, c + dc
    cell = grid[nr][nc]
    if cell == '.':
        grid[nr][nc] = grid[r][c]
        grid[r][c] = '.'
        return
    if dc != 0:
        do_push_wide(grid, nr, nc, dr, dc)
        grid[nr][nc] = grid[r][c]
        grid[r][c] = '.'
        return
    if cell == '[':
        do_push_wide(grid, nr, nc, dr, dc)
        do_push_wide(grid, nr, nc + 1, dr, dc)
        grid[nr][nc] = grid[r][c]
        grid[r][c] = '.'
    elif cell == ']':
        do_push_wide(grid, nr, nc, dr, dc)
        do_push_wide(grid, nr, nc - 1, dr, dc)
        grid[nr][nc] = grid[r][c]
        grid[r][c] = '.'

for move in moves:
    dr, dc = dir_map[move]
    nr, nc = robot_r + dr, robot_c + dc
    cell = grid2[nr][nc]
    if cell == '#':
        continue
    if cell == '.':
        robot_r, robot_c = nr, nc
    else:
        if can_push_wide(grid2, robot_r, robot_c, dr, dc):
            do_push_wide(grid2, robot_r, robot_c, dr, dc)
            robot_r, robot_c = nr, nc

gps2 = sum(100 * r + c for r in range(rows2) for c in range(cols2) if grid2[r][c] == '[')
print(gps2)
