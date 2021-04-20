num1 = int(input('첫번째 숫자를 넣어주세요 : '))
num2 = int(input('두번째 숫자를 넣어주세요 : '))
num3 = int(input('세번째 숫자를 넣어주세요 : '))
print('세 수는', num1, ',',num2,',',num3,'입니다.')

if num1 >= num2 and num1 >= num3 :
    print('가장 큰 수는 ' + str(num1)+ ' 입니다.')
if num2 > num1 and num2 >= num3 :
    print('가장 큰 수는 ' + str(num2)+ ' 입니다.')
if num3 > num1 and num3 > num2 :
    print('가장 큰 수는 ' + str(num3)+ ' 입니다.')
    
if num1 <= num2 and num1 <= num3 :
    print('가장 작은 수는 ' + str(num1)+ ' 입니다.')
if num2 < num1 and num2 <= num3 :
    print('가장 작은 수는 ' + str(num2)+ ' 입니다.')
if num3 < num1 and num3 < num2 :
    print('가장 작은 수는 ' + str(num3)+ ' 입니다.')