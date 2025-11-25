
from sortedcontainers import SortedDict

with open('input_day5','r',encoding="utf-8") as f:
    input = f.read()

#part1

rules = input.split('\n\n')[0]
updates = input.split('\n\n')[1]
r1 = rules.split('|')[0]

r1= list(map(lambda rule: rule.strip().split('|'), rules.split('\n'))) #rules
u1= list(map(lambda update: update.strip().split(','), updates.split('\n'))) #update

r2 = SortedDict()

#tentative de tri des regles
#faire un abr ffsdgsdgf
# FEFREGTRHYNB TROP CON
#r2.update(r1)
"""for i in range(0,len(r1)):
    if r1[i][0] in r2:
        if r2.index(r1[i][0]) > r2.index(r1[i][1]):
            tmp = r2[r2.index(r1[i][0])]
            r2[r2.index(r1[i][0])] = r2[r2.index(r1[i][1])]
            r2[r2.index(r1[i][1])] = tmp"""

pile = []

def partie1(u1,r1):
    total = 0
    for i in range(0,len(u1)):
        isCorrect = 1
        for j in range(0,len(u1[i])): #construit pile depuis update i
            pile.append(u1[i][j]) 
        print(pile)
        for j in range(0,len(pile)-1):
            for k in range(j+1,len(pile)-1):
                if list([pile[k], pile[j]]) in r1: #règle k avant j
                    isCorrect = 0
        pile.clear()
        if isCorrect == 1:
            total = total + int(u1[i][len(u1[i])//2])
        print(total)
        
def partie2(u1,r1):
    u2 = list()
    total = 0
    for i in range(0,len(u1)):
        isCorrect = 1
        for j in range(0,len(u1[i])): #construit pile depuis update i
            pile.append(u1[i][j]) 
        print(pile)
        for j in range(0,len(pile)-1):
            for k in range(j+1,len(pile)-1):
                if list([pile[k], pile[j]]) in r1: #règle k avant j
                    isCorrect = 0
        pile.clear()
        if isCorrect == 0:
            u2.append(u1[i])
    print(u2[len(u2)-2])
    for i in range(0,len(r1)):
        if r1[i][0] in u2[len(u2)-2] and r1[i][1] in u2[len(u2)-2]:
            print(r1[i])
    #règles correctes supprimées
    
    for i in range(0,len(u2)):
        err = 0
        for j in range(0,len(u2[i])): #construit pile depuis update i
            pile.append(u2[i][j]) 
        print(pile)
        for m in range(0,len(pile)-1):
            for j in range(0,len(pile)):
                for k in range(j+1,len(pile)):
                    if list([pile[k], pile[j]]) in r1: #règle k avant j
                        tmp = pile[j]
                        pile[j] = pile[k]
                        pile[k] = tmp #correction (partie qui marche pas imo)
                        err = err+1
        for j in range(0,len(pile)): #construit pile depuis update i
            u2[i][j] = pile[j]
        print("res: "+str(u2[i]))
        print("err: "+str(err))
        pile.clear()
        total = total + int(u2[i][len(u2[i])//2])
        print(total)

#print(u1)
partie2(u1,r1)

