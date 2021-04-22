## Quick sort : 기준숫자보다 작은 것 왼쪽, 큰 것 오른쪽으로
quick = [7, 1, 9, 13, 3, 17, 4, 6, 4, 2, 8]
rlwns = 8
left = []
middle = []
right = []
cnt=0

for i in range(0,len(quick)):
    if quick[i] < 8:
        left.append(quick[i])
    if quick[i] == 8:
        middle.append(quick[i])
    if quick[i] > 8:
        right.append(quick[i])

quick = left + middle + right

print(quick)
