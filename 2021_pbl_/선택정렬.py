## 선택정렬 : 가장 작은것부터 앞으로
numbers = [7, 1, 3, 6, 8, 9, 2]
cnt=0
while cnt < len(numbers):
    min = 10
    for number in numbers[cnt:]:
        if min > number:
            min = number
    print('min:' , min)
    minIndex = numbers.index(min)
    print('min_index:' , numbers.index(min))
    numbers[minIndex] = numbers[cnt]
    numbers[cnt] = min
    cnt=cnt+1
    print(numbers)
    print( ' ')
