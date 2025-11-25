#! /bin/python3

with open('input_day2','r',encoding="utf-8") as f:
    input = f.read()

records = input.splitlines()

#part1

def isSafe(record):
    j = 0
    asc = 0
    desc = 0
    unsafe = 0
    while j < len(record)-1:
        if int(record[j]) < int(record[j+1]):
            if desc != 1:
                asc = 1
            else:
                unsafe = 1
        else:
            if asc != 1:
                desc = 1
            else:
                unsafe = 1
        if (int(record[j]) - int(record[j+1]) > 3 and desc==1) or (int(record[j]) - int(record[j+1]) < -3 and asc==1) or (int(record[j]) - int(record[j+1]) == 0):
            unsafe = 1
        j = j+1
    if not unsafe:
        return 1
    else:
        return 0

safe = 0
record = []
for i in range(0,len(records)):
    record = records[i].split(' ')
    safe = safe + isSafe(record)
print(safe)

#part2

safe = 0
record = []
for i in range(0,len(records)):
    record = records[i].split(' ')
    if (isSafe(record)):
        safe = safe+1
    else:
        rec_tmp = []
        for j in range(0,len(record)):
            rec_tmp = record.copy()
            rec_tmp.pop(j)
            if (isSafe(rec_tmp)):
                safe = safe + 1
                break
print(safe)