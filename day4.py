#! /bin/python3

with open('input_day4','r',encoding="utf-8") as f:
    input = f.read()

#part1

#comme recherche d'image : trouver un X = recherche cardinale
#  . . .    NO N NE
#  . X .  => O X E
#  . . .    SO S SE

t_column = input.find('\n')
rows = input.split('\n')
t_row = len(rows)-1

xmas_count = 0
print(t_row,t_column)
for i in range(0,t_row):
    for j in range(0,t_column):
        if rows[i][j] == 'X':
            if j < t_column-3: # E
                if rows[i][j+1] == 'M' and rows[i][j+2] == 'A' and rows[i][j+3] == 'S':
                    xmas_count = xmas_count+1
                if i >= 3: #NE
                    if rows[i-1][j+1] == 'M' and rows[i-2][j+2] == 'A' and rows[i-3][j+3] == 'S':
                        xmas_count = xmas_count+1
                if i < t_row-3: #SE
                    if rows[i+1][j+1] == 'M' and rows[i+2][j+2] == 'A' and rows[i+3][j+3] == 'S':
                        xmas_count = xmas_count+1
            if i < t_row-3: #S
                if rows[i+1][j] == 'M' and rows[i+2][j] == 'A' and rows[i+3][j] == 'S':
                    xmas_count = xmas_count+1
            if i >= 3: #N
                if rows[i-1][j] == 'M' and rows[i-2][j] == 'A' and rows[i-3][j] == 'S':
                    xmas_count = xmas_count+1
            if j >= 3: #O
                if rows[i][j-1] == 'M' and rows[i][j-2] == 'A' and rows[i][j-3] == 'S':
                    xmas_count = xmas_count+1
                if i >= 3: #NO
                    if rows[i-1][j-1] == 'M' and rows[i-2][j-2] == 'A' and rows[i-3][j-3] == 'S':
                        xmas_count = xmas_count+1
                if i < t_row-3: #SO
                    if rows[i+1][j-1] == 'M' and rows[i+2][j-2] == 'A' and rows[i+3][j-3] == 'S':
                        xmas_count = xmas_count+1
print(xmas_count)

#part2
# . . ? . .     ? . M . ?
# . . . . .     . ? . ? .
# ? . M . ?  => ? . M . ? X
# . . . . .     . . . . .
# . . ? . .     . . . . .

# . . .
# . A .
# . . .

xmas_count = 0

for i in range(0,t_row):
    for j in range(0,t_column):
        if rows[i][j] == 'A':
            if j < t_column-1 and j >= 1 and i < t_row-1 and i >= 1: #space for xmas
                if rows[i-1][j-1] == 'M' and rows[i-1][j+1] == 'M' and rows[i+1][j-1] == 'S' and rows[i+1][j+1] == 'S':
                    xmas_count = xmas_count+1
                if rows[i-1][j-1] == 'S' and rows[i-1][j+1] == 'M' and rows[i+1][j-1] == 'S' and rows[i+1][j+1] == 'M':
                    xmas_count = xmas_count+1
                if rows[i-1][j-1] == 'S' and rows[i-1][j+1] == 'S' and rows[i+1][j-1] == 'M' and rows[i+1][j+1] == 'M':
                    xmas_count = xmas_count+1
                if rows[i-1][j-1] == 'M' and rows[i-1][j+1] == 'S' and rows[i+1][j-1] == 'M' and rows[i+1][j+1] == 'S':
                    xmas_count = xmas_count+1
                
print(xmas_count)