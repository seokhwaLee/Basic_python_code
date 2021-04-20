import random

while True:
    # 사용자 결정-------------------------------------------------------
    yourHand = input('가위~ 바위~ 보 ! 중에 하나를 골라주세요~   ')
    print ()

    # 컴퓨터 결정-------------------------------------------------------
    comRandom = random.randint(1,3)  # uniformly distributed random number generator
    if comRandom == 1:
        comHand = '가위'
    elif comRandom == 2:
        comHand = '바위'
    else:
        comHand = '보'

    # 승부판단 및 출력 -------------------------------------------------------
    if comHand == yourHand:
        print ('무승부! 또 해! (You:' + yourHand + '~, Com:' + comHand + '~)')
    elif (comHand=='바위' and yourHand=='가위') or (comHand=='가위' and yourHand=='보') or (comHand=='보' and yourHand=='바위'):
        print ('당신 짐! 컴퓨터 이김! 또 해! (You:' + yourHand + '~, Com:' + comHand + '~)')
    else: ## 사용자가 이기는 경우
        print ('당신 이김! 컴퓨터 짐! (You:' + yourHand + '~, Com:' + comHand + '~)')
        break 