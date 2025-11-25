#! /usr/bin/env python3
with open('input_day6','r',encoding="utf-8") as f:
    input = f.read()
    f.seek(0,0)
    col_len = len(f.readline())
    li_len = len(input)//col_len

#part1
def partie1(input):
    input = list(input)
    gx = 0
    gy = 0
    for i in range(0,li_len):
        for j in range(0,col_len):
            if input[j+(i*col_len)] == '^':
                gx = j
                gy = i
                input[gx+col_len*gy] = 'X'

    isOOB = False
    d = 'up'
    while not isOOB:
        print(d)
        match d:
            case 'up':
                if gy != 0 and input[gx+col_len*(gy-1)] == '.' or input[gx+col_len*(gy-1)] == 'X':
                    gy = gy-1
                    input[gx+col_len*gy] = 'X'
                else:
                    if gy == 0:
                        isOOB = True
                    d = 'right'
            case 'right':
                if gx != col_len-1 and input[(gx+1)+col_len*(gy)] == '.' or input[(gx+1)+col_len*(gy)] == 'X':
                    gx = gx+1
                    input[gx+col_len*gy] = 'X'
                else:
                    if gx == col_len-1:
                        isOOB = True
                    d = 'down'
            case 'down':
                if gy != li_len-1 and (input[gx+col_len*(gy+1)] == '.' or input[gx+col_len*(gy+1)] == 'X'):
                    gy = gy+1
                    input[gx+col_len*gy] = 'X'
                else:
                    if gy == li_len-1:
                        isOOB = True
                    d = 'left'
            case 'left':
                if gx != 0 and input[(gx-1)+col_len*(gy)] == '.' or input[(gx-1)+col_len*(gy)] == 'X':
                    gx = gx-1
                    input[gx+col_len*gy] = 'X'
                else:
                    if gx == 0:
                        isOOB = True
                    d = 'up'

    total = 0
    for i in range(0,li_len):
        for j in range(0,col_len):
            if input[j+(i*col_len)] == 'X':
                total = total + 1
    print(total)

#part2

def noDash(input, li_len, col_len):
    for i in range(0,li_len):
        for j in range(0,col_len):
            if input[j+(i*col_len)] == '-':
                input[j+(i*col_len)] = '.'
            if input[j+(i*col_len)] == '*':
                input[j+(i*col_len)] = 'X'

def partie2(input):
    input = list(input)
    gx = 0
    gy = 0
    for i in range(0,li_len):
        for j in range(0,col_len):
            if input[j+(i*col_len)] == '^':
                gx = j
                gy = i
                input[gx+col_len*gy] = 'X'

    isOOB = False
    position = list()
    d = 'up'
    l = 0
    while not isOOB:
        l = l+1
        print(str(l)+':'+d+str(len(position)))
        match d:
            case 'up':
                tmp = dejavu(input, gx,gy,d)
                noDash(input,li_len,col_len)
                if (tmp != None and tmp not in position):
                    position.append(tmp)
                if gy != 0 and input[gx+col_len*(gy-1)] == '.' or input[gx+col_len*(gy-1)] == 'X':
                    gy = gy-1
                    input[gx+col_len*gy] = 'X'
                else:
                    if gy == 0:
                        isOOB = True
                    d = 'right'
            case 'right':
                tmp = dejavu(input, gx,gy,d)
                noDash(input,li_len,col_len)
                if (tmp != None and tmp not in position):
                    position.append(tmp)
                if gx != col_len-1 and input[(gx+1)+col_len*(gy)] == '.' or input[(gx+1)+col_len*(gy)] == 'X':
                    gx = gx+1
                    input[gx+col_len*gy] = 'X'
                else:
                    if gx == col_len-1:
                        isOOB = True
                    d = 'down'
            case 'down':
                tmp = dejavu(input, gx,gy,d)
                noDash(input,li_len,col_len)
                if (tmp != None and tmp not in position):
                    position.append(tmp)
                if gy != li_len-1 and (input[gx+col_len*(gy+1)] == '.' or input[gx+col_len*(gy+1)] == 'X'):
                    gy = gy+1
                    input[gx+col_len*gy] = 'X'
                else:
                    if gy == li_len-1:
                        isOOB = True
                    d = 'left'
            case 'left':
                tmp = dejavu(input, gx,gy,d)
                noDash(input,li_len,col_len)
                if (tmp != None and tmp not in position):
                    position.append(tmp)
                if gx != 0 and input[(gx-1)+col_len*(gy)] == '.' or input[(gx-1)+col_len*(gy)] == 'X':
                    gx = gx-1
                    input[gx+col_len*gy] = 'X'
                else:
                    if gx == 0:
                        isOOB = True
                    d = 'up'
    print(len(position))
    
def dejavu(input, gx, gy,gd):
    type(input)
    x = gx
    y = gy
    d = gd
    coord = list()
    visite = False
    while not visite:
#        print("xplore "+d+",coord:"+str(len(coord)))
        match d:
            case 'up':
             #exploration pos à 90° (à droite)
                while x != col_len-1 and input[(x+1)+col_len*y] != '#':
                    x = x+1
                    if (input[x+col_len*y] == 'X' or input[x+col_len*y] == '-'):
                        input[x+col_len*y] = '*'
                    else:
                        input[x+col_len*y] = '-'
                if x != col_len-1 and (input[x+col_len*y] == 'X' or input[x+col_len*y] == '*'):
                    coord.append(x)
                    coord.append(y)
                    visite = True
                else:
                    if x == col_len-1:
                        visite = True
                    y = y-1
                    d = 'right'
            case 'right':
                #exploration pos à 90° (en bas)
                while y != li_len-1 and input[x+col_len*(y+1)] != '#':
                    y = y+1                    
                    if (input[x+col_len*y] == 'X' or input[x+col_len*y] == '-'):
                        input[x+col_len*y] = '*'
                    else:
                        input[x+col_len*y] = '-'
                if y != li_len-1 and (input[x+col_len*y] == 'X' or input[x+col_len*y] == '*'):
                    coord.append(x)
                    coord.append(y)
                    visite = True
                else:
                    if y == li_len-1:
                        visite = True
                    x = x+1
                    d = 'down'
            case 'down':
            #exploration pos à 90° (à gauche)
                #exploration pos à 90°
                while x != 0 and input[(x-1)+col_len*y] != '#':
                    x = x-1                    
                    if (input[x+col_len*y] == 'X' or input[x+col_len*y] == '-'):
                        input[x+col_len*y] = '*'
                    else:
                        input[x+col_len*y] = '-'
                if x != 0 and (input[x+col_len*y] == 'X' or input[x+col_len*y] == '*'):
                    coord.append(x)
                    coord.append(y)
                    visite = True
                else:
                    if x == 0:
                        visite = True
                    y = y+1
                    d = 'left'
            case 'left':
                #exploration pos à 90° (en haut)
                while y != 0 and input[x+col_len*(y-1)] != '#':
                    y = y-1
                    if (input[x+col_len*y] == 'X' or input[x+col_len*y] == '-'):
                        input[x+col_len*y] = '*'
                    else:
                        input[x+col_len*y] = '-'
                if y != 0 and (input[x+col_len*y] == 'X' or input[x+col_len*y] == '*'):
                    coord.append(x)
                    coord.append(y)
                    visite = True
                else:
                    if y == 0:
                        visite = True
                    x = x-1
                    d = 'up'
    #print("coord:"+str(coord))
    if len(coord) > 0:
        return coord
    else:
        return None
partie2(input)
