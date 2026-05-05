#!/usr/bin/env python3
# Written by claude

with open('input_day7', 'r', encoding='utf-8') as f:
    data = f.read().strip()

lines = data.splitlines()
equations = []
for line in lines:
    left, right = line.split(': ')
    target = int(left)
    nums = list(map(int, right.split()))
    equations.append((target, nums))

def can_make(target, nums, use_concat=False):
    def evaluate(nums, idx, current):
        if idx == len(nums):
            return current == target
        n = nums[idx]
        if evaluate(nums, idx + 1, current + n):
            return True
        if evaluate(nums, idx + 1, current * n):
            return True
        if use_concat:
            concatenated = int(str(current) + str(n))
            if evaluate(nums, idx + 1, concatenated):
                return True
        return False
    return evaluate(nums, 1, nums[0])

# Part 1: operators + and *
total1 = sum(target for target, nums in equations if can_make(target, nums, False))
print(total1)

# Part 2: operators +, *, and ||
total2 = sum(target for target, nums in equations if can_make(target, nums, True))
print(total2)
