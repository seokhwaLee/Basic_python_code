## 로또 번호 생성 & 당첨 확인 프로그램
import random

def number():
    list_num = []
    cnt = 0
    while cnt < 6:
        list_num.append(int(input('1~45사이의 숫자 6개를 입력하세요')))
        cnt = cnt + 1
    return list_num

def lotto():
    listA = list(range(1,46))
    random.shuffle(listA)
    list_lot = listA[:6]
    return list_lot

def match(list_num, list_lot):
    result = []
    for num in list_num:
        for lot in list_lot:
            if num == lot:
                result.append(num)
    return result

def money(same) :
    if len(same) < 3 :
        result = '꽝'
    if len(same) == 3:
        result = '당첨'

print('복권 번호를 맞춰보세요!')
remain = int(input('얼마를 넣으시겠습니까? '))
while remain >= 1000:
    userlist = number()
    lottolist = lotto()
    print('이번주 복권 번호는', lottolist, '입니다.')
    matchlist = match(lottolist, userlist)
    print('맞춘 숫자는', matchlist, '입니다.')
    prizelist = [0,0,0,0,5000,10000,50000]
    prize = prizelist[len(matchlist)]
    print(len(matchlist), '개를 맞춰 당첨금은', prize, '원입니다.')
    print()
    remain = remain - 1000
    print('그만 하시겠습니까? 예/아니오')
    answer = input()
    if answer == '예':
        print('거스름돈은', remain, '원 입니다.')
        break