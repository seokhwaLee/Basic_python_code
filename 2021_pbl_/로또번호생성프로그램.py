## 로또 번호 생성 프로그램

import random

# print ('로또 번호 생성 프로그램')
# print ('=====================')

# lotto = 0

# while lotto < 6:
#    number = str(random.randint(1, 45))
#    print (str(lotto+1)+'번째 번호는 ' + number + '입니다.')
#    lotto = lotto + 1

print ('=====================')
end = 45
cnt = 1  # 무작위 선택을 몇번 했는지 궁금해서.
number1 = str(random.randint(1, end))
while True :
    number2 = str(random.randint(1, end))
    cnt = cnt + 1
    if (number1 != number2) : # 조건식1
        number3 = str(random.randint(1, end))
        cnt = cnt + 1
        if (number1 != number3) and (number2 != number3) : #조건식2
            number4 = str(random.randint(1, end))
            cnt = cnt + 1
            if (number1 != number4) and (number2 != number4) and (number3 != number4) : #조건식3
                number5 = str(random.randint(1, end))
                cnt = cnt + 1
                if (number1 != number5) and (number2 != number5) and (number3 != number5) and (number4 != number5) :
                    number6 = str(random.randint(1, end))
                    cnt = cnt + 1
                    if (number1 != number6) and (number2 != number6) and (number3 != number6) and (number4 != number6) and (number5 != number6):
                        print ('1번째 번호는 ' + number1 + '입니다.')
                        print ('2번째 번호는 ' + number2 + '입니다.')
                        print ('3번째 번호는 ' + number3 + '입니다.')
                        print ('4번째 번호는 ' + number4 + '입니다.')
                        print ('5번째 번호는 ' + number5 + '입니다.')
                        print ('6번째 번호는 ' + number6 + '입니다.')
                        break
print (cnt)