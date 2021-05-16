## 키오스크 만들기

print('haru cafe에 오신것을 환영합니다🎉💕')
print('무엇을 드시겠습니까???')
extra = 1
while extra > 0:
    select = input('커피☕, 음료🧉, 디저트🍰 : ')
    cnt = 0
    if select == '커피':
        while cnt < 1 :
            menu= input('아메리카노, 모카라떼, 카라멜마끼야또, 에스프레소 중 무엇을 드시고 싶으세요? : ')
            if menu == '아메리카노' or menu == '모카라떼' or menu == '카라멜마끼야또' or menu == '에스프레소':
                print(menu + '를 선택하시겠습니까?')
                cnt = int(input('맞다면 1, 아니면 0을 눌러주세요! : '))
            else :
                print('다시 입력해주세요ㅠㅠ')
                print(' ')
            
        print('>>>'+ menu + '를 선택하셨습니다.')
        print(' ')
        extra = int(input('추가주문을 하시겠습니까? 맞다면 1, 아니면 0을 눌러주세요!'))

    cnt=0
    if select == '음료':
        while cnt < 1 :
            menu= input('초코라떼, 녹차라떼, 요거트프라푸치노, 생딸기주스 중 무엇을 드시겠어요? : ')
            if menu == '초코라떼' or menu == '녹차라떼' or menu == '요거트프라푸치노' or menu == '생딸기주스':
                print(menu + '를 선택하시겠습니까?')
                cnt = int(input('맞다면 1, 아니면 0을 눌러주세요! : '))
            else :
                print('다시 입력해주세요ㅠㅠ')
                print(' ')
            
        print('>>>'+ menu + '를 선택하셨습니다.')
        print(' ')
        extra = int(input('추가주문을 하시겠습니까? 맞다면 1, 아니면 0을 눌러주세요! : '))

    cnt=0
    if select == '디저트':
        while cnt < 1 :
            menu= input('초코케이크, 딸기생크림케이크, 브라우니, 허니브레드 중 무엇을 드시고 싶으세요? : ')
            if menu == '초코케이크' or menu == '딸기생크림케이크' or menu == '브라우니' or menu == '허니브레드':
                print(menu + '를 선택하시겠습니까?')
                cnt = int(input('맞다면 1, 아니면 0을 눌러주세요! : '))
            else :
                print('다시 입력해주세요ㅠㅠ')
                print(' ')
        
        print('>>>'+ menu + '를 선택하셨습니다.')  
        print(' ')
        extra = int(input('추가주문을 하시겠습니까? 맞다면 1, 아니면 0을 눌러주세요! : '))

print('어떤 방법으로 결제하시겠습니까? ')
pay = input('신용카드, 현금 : ')
print(' ')

if pay == '신용카드':
    print('카드를 넣어주세요.')
    print('결제가 완료되었습니다. 카드를 제거해주세요.')
if pay == '현금':
    print('카운터에 문의해주세요!!')
