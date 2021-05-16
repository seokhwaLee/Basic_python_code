## 삽입정렬 : 두번째숫자부터 앞의 숫자들과 비교, 작으면 앞으로
listA = [3,6,8,5,4,2,6,1]
for j in range(1,len(listA)):
    key = listA[j]
    i = j-1
    while i >= 0 and listA[i] > key:
        listA[i+1] = listA[i]
        i = i - 1
        listA[i + 1] = key
    print(listA)
