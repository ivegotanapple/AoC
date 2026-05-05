#!/usr/bin/env python3
# Written by claude

from functools import lru_cache

with open('input_day19', 'r', encoding='utf-8') as f:
    data = f.read().strip()

patterns_part, designs_part = data.split('\n\n')
patterns = tuple(p.strip() for p in patterns_part.split(','))
designs = designs_part.splitlines()

@lru_cache(maxsize=None)
def count_ways(design):
    if not design:
        return 1
    total = 0
    for p in patterns:
        if design.startswith(p):
            total += count_ways(design[len(p):])
    return total

possible = 0
total_ways = 0
for design in designs:
    ways = count_ways(design)
    if ways > 0:
        possible += 1
    total_ways += ways

# Part 1: count designs that can be made
print(possible)
# Part 2: total number of ways to make each design
print(total_ways)
