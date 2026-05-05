#!/usr/bin/env python3
# Written by claude

import re

with open('input_day17', 'r', encoding='utf-8') as f:
    data = f.read().strip()

nums = list(map(int, re.findall(r'\d+', data)))
init_A, init_B, init_C = nums[0], nums[1], nums[2]
program = nums[3:]

def run(A, B, C, program):
    ip = 0
    output = []

    def combo(operand):
        if operand <= 3:
            return operand
        if operand == 4:
            return A
        if operand == 5:
            return B
        if operand == 6:
            return C
        raise ValueError(f'invalid combo operand {operand}')

    while ip < len(program):
        op = program[ip]
        operand = program[ip + 1]
        ip += 2
        if op == 0:  # adv
            A = A >> combo(operand)
        elif op == 1:  # bxl
            B = B ^ operand
        elif op == 2:  # bst
            B = combo(operand) % 8
        elif op == 3:  # jnz
            if A != 0:
                ip = operand
        elif op == 4:  # bxc
            B = B ^ C
        elif op == 5:  # out
            output.append(combo(operand) % 8)
        elif op == 6:  # bdv
            B = A >> combo(operand)
        elif op == 7:  # cdv
            C = A >> combo(operand)

    return output

# Part 1
result = run(init_A, init_B, init_C, program)
print(','.join(map(str, result)))

# Part 2: find A such that program outputs itself
# Work backwards digit by digit - each output digit depends on 3 bits of A
# Program produces one output per iteration, A is shifted right by 3 each time
def find_quine(program, target_idx, current_A):
    if target_idx < 0:
        return current_A
    target = program[target_idx]
    for bits in range(8):
        candidate_A = (current_A << 3) | bits
        out = run(candidate_A, init_B, init_C, program)
        if out and out[0] == target:
            result = find_quine(program, target_idx - 1, candidate_A)
            if result is not None:
                return result
    return None

answer = find_quine(program, len(program) - 1, 0)
print(answer)
