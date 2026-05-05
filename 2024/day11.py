#!/usr/bin/env python3
# Written by claude

from collections import Counter

with open('input_day11', 'r', encoding='utf-8') as f:
    data = f.read().strip()

stones = Counter(map(int, data.split()))

def blink(stones):
    new_stones = Counter()
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            mid = len(s) // 2
            new_stones[int(s[:mid])] += count
            new_stones[int(s[mid:])] += count
        else:
            new_stones[stone * 2024] += count
    return new_stones

# Part 1: 25 blinks
s = Counter(stones)
for _ in range(25):
    s = blink(s)
print(sum(s.values()))

# Part 2: 75 blinks
s = Counter(stones)
for _ in range(75):
    s = blink(s)
print(sum(s.values()))
