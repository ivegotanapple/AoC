#! /bin/python3


with open('input_day1','r',encoding="utf-8") as f:
    input = f.read()
    
#part 1    
left = []
right = []
for i in range(0,len(input.split())):
    if i%2==0:
        left.append(input.split()[i])
    else:
        right.append(input.split()[i])

left = list(map(int,left))
right = list(map(int,right))

left.sort()
right.sort()
sum = 0
for i in range(0,len(left)):
    if left[i] > right[i]:
        sum = sum + (left[i] - right[i])
    else:
        sum = sum + (right[i] - left[i])

print(sum)

#part 2
score = 0
for i in range(0,len(left)):
    count = 0
    for j in range(0,len(right)):
        if left[i] == right[j]:
            count = count + 1
    score = score + count*left[i]
print(score)
