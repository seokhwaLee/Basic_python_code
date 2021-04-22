##함수사용해 이길때까지 가위바위보
import random
def decideRSP():
    listA = []
    listA.append(input('가위~ 바위~ 보 ! 중에 하나를 골라주세요~ ')) # 사용자 결정
    
    # 컴퓨터 결정-------------------------------------------------------
    comRandom = random.randint(1,3) # uniformly distributed random number generator
    if comRandom == 1:
        listA.append('가위')
    elif comRandom == 2:
        listA.append('바위')
    else:
        listA.append('보')
    
    return listA
 
def decideWinner(listA):
    if listA[0] == listA[1]:
        print ('무승부! 또 해! (You:' + listA[0] + '~, Com:' + listA[1] + '~)')
        winner = "none"
    elif (listA[0]=='바위' and listA[1]=='가위') or (listA[0]=='가위' and listA[1]=='보') or (listA[0]=='보' and listA[1]=='바위'):
        print ('당신 짐! 컴퓨터 이김! 또 해! (You:' + listA[0] + '~, Com:' + listA[1] + '~)')
        winner = '컴퓨터'
    else: ## 사용자가 이기는 경우
        print ('당신 이김! 컴퓨터 짐! (You:' + listA[0] + '~, Com:' + listA[1] + '~)')
        winner = '사용자'
    
    return winner
 
while True:
    result = decideWinner(decideRSP())
    if result == '사용자':
        break
