#처음 짠 코드
def solution(lottos, win_nums):
    cnt=0
    wnum = 0
    for lot in lottos:
        if lot in win_nums:
            cnt +=1
        if lot == 0:
            wnum +=1
    max_tnsdnl = cnt + wnum
    min_tnsdnl = cnt
    numbers = [max_tnsdnl,min_tnsdnl]
    answer = []
    for i in range(2):
        if numbers[i] == 2:
            answer.append(5)
        elif numbers[i] == 3:
            answer.append(4)
        elif numbers[i] == 4:
            answer.append(3)
        elif numbers[i] == 5:
            answer.append(2)
        elif numbers[i] == 6:
            answer.append(1)
        else:
            answer.append(6)            
    return answer

# 코드 단순화
def solution2(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    answer = [rank[cnt_0 + ans], rank[ans]]
    return answer