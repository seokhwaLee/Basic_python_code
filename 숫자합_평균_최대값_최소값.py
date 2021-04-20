import random
print('숫자를 입력하세요. 입력이 끝나면 /'입력끝/'을 입력하세요')
num = 0
cnt = 0
sum_num=0
mean = 0
biggest = 0
smallest = 100000000
nt = 0

while nt < 5:
    numm = input()
    cnt = cnt + 1
    if numm == '입력 끝' : 
        nt = 5
    
    else :
        num = int(numm)
        if biggest < num:
            biggest = num

        if smallest > num:
            smallest = num

        sum_num= sum_num + num
        mean = sum_num/cnt
    
        
print('입력받은 숫자들의 합은', sum_num)
print('입력받은 숫자들의 평균은', mean)
print('가장 큰 숫자는', biggest)
print('가장 작은 숫자는', smallest)