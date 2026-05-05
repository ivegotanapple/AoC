#!/usr/bin/env python3
# Written by claude

from collections import defaultdict

with open('input_day22', 'r', encoding='utf-8') as f:
    data = f.read().strip()

initial_secrets = list(map(int, data.splitlines()))

MOD = 16777216  # 2^24

def next_secret(s):
    s = ((s * 64) ^ s) % MOD
    s = ((s // 32) ^ s) % MOD
    s = ((s * 2048) ^ s) % MOD
    return s

# Part 1: sum of 2000th secrets
total1 = 0
for s in initial_secrets:
    for _ in range(2000):
        s = next_secret(s)
    total1 += s
print(total1)

# Part 2: find best 4-change sequence
sequence_bananas = defaultdict(int)

for s in initial_secrets:
    prices = [s % 10]
    cur = s
    for _ in range(2000):
        cur = next_secret(cur)
        prices.append(cur % 10)
    changes = tuple(prices[i] - prices[i - 1] for i in range(1, len(prices)))
    seen = set()
    for i in range(len(changes) - 3):
        seq = changes[i:i + 4]
        if seq not in seen:
            seen.add(seq)
            sequence_bananas[seq] += prices[i + 4]

print(max(sequence_bananas.values()))
