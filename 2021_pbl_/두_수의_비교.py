num1 = int(input('첫번째 숫자를 넣어주세요 : '))
num2 = int(input('두번째 숫자를 넣어주세요 : '))

if num1 == num2 : #두 수가 같은 경우 출력
    print('두 수는 같습니다. ')
    
if num1 != num2 : # 두 수가 다른 경우 출력
    print('두 수는 다릅니다. ')
    print('두 숫자는 ' + str(num1) + '과 ' + str(num2) + ' 입니다.')