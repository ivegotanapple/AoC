#!/usr/bin/env python3
# Written by claude

with open('input_day9', 'r', encoding='utf-8') as f:
    data = f.read().strip()

# Parse disk map into blocks: list of (file_id or None for free space)
def parse_disk(data):
    blocks = []
    file_id = 0
    for i, ch in enumerate(data):
        length = int(ch)
        if i % 2 == 0:
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend([None] * length)
    return blocks

# Part 1: move individual file blocks from right to leftmost free space
blocks = parse_disk(data)
disk = blocks[:]
left = 0
right = len(disk) - 1
while left < right:
    while left < right and disk[left] is not None:
        left += 1
    while left < right and disk[right] is None:
        right -= 1
    if left < right:
        disk[left] = disk[right]
        disk[right] = None
        left += 1
        right -= 1

checksum1 = sum(i * v for i, v in enumerate(disk) if v is not None)
print(checksum1)

# Part 2: move whole files right-to-left into leftmost fitting gap
blocks = parse_disk(data)

# Find file spans: {file_id: (start, length)}
file_spans = {}
i = 0
while i < len(blocks):
    if blocks[i] is not None:
        fid = blocks[i]
        start = i
        while i < len(blocks) and blocks[i] == fid:
            i += 1
        file_spans[fid] = (start, i - start)
    else:
        i += 1

max_file_id = max(file_spans.keys())

for fid in range(max_file_id, -1, -1):
    fstart, flen = file_spans[fid]
    # Find leftmost free span of length >= flen before fstart
    gap_start = None
    gap_len = 0
    for j in range(fstart):
        if blocks[j] is None:
            if gap_start is None:
                gap_start = j
            gap_len += 1
            if gap_len >= flen:
                break
        else:
            gap_start = None
            gap_len = 0

    if gap_start is not None and gap_len >= flen:
        # Move file to gap_start
        for k in range(flen):
            blocks[gap_start + k] = fid
            blocks[fstart + k] = None
        file_spans[fid] = (gap_start, flen)

checksum2 = sum(i * v for i, v in enumerate(blocks) if v is not None)
print(checksum2)
