num= int(input('숫자를 입력해 주세요'))

remainder = num % 2

if remainder == 0 :
    print (str(num) + ' 은 짝수입니다. ')

if remainder != 0 :
    print (str(num) + ' 은 홀수입니다. ')