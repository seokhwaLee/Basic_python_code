## Counting Sort
import random
listA = []
cnt = 0
while cnt<20:
    listA.append(random.randint(1,7))
    cnt=cnt+1

countlist = [0,0,0,0,0,0,0]

for i in range(1,8):
    cnt = 0
    for j in listA:
        if i == j :
            cnt= cnt+1
        countlist[i-1] = cnt
print(listA, countlist)

listB = []

n=1
for qjs in countlist:
    while qjs > 0 :
        listB.append(n)
        qjs = qjs -1
    n=n+1
print(listB)
