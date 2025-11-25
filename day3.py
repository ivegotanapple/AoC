#! /bin/python3

with open('input_day3','r',encoding="utf-8") as f:
    input = f.read()

#part1

import re 
p = re.compile(r'mul\(\d{1,3}\,\d{1,3}\)')
mul = p.findall(input)

q = re.compile(r'mul\(|\)')
r = re.compile(r'\,')

total = 0
for i in range(0,len(mul)):
    mul[i] = q.sub('',mul[i])
    tmp = r.split(mul[i])
    total = total + (int(tmp[0]) * int(tmp[1]))

print(total)

#part2

mulp = re.compile(r'mul\(\d{1,3}\,\d{1,3}\)')
dop = re.compile(r'do\(.*\)')
dontp = re.compile(r'don\'t\(.*\)')

ind_mul = 0
total = 0
disabled = 0

for i in range(0,len(input)):
    m = mulp.match(input[i:])
    d = dop.match(input[i:])  
    dn = dontp.match(input[i:])
    if dn:
        disabled = 1
        lastdn = dn
    if m and not disabled:
        tmp = r.split(mul[ind_mul])
        total = total + (int(tmp[0]) * int(tmp[1]))
        ind_mul = ind_mul+1
    else:
        if m:
            ind_mul = ind_mul+1
    if d:
        disabled = 0
        lastd = d

print(total)