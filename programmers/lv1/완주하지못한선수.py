# 나의 풀이
## for문 사용해서 값 1개씩 비교
def solution(participant, completion):
    for no in participant:
        if no not in completion:
            answer = no
        else :
            completion.remove(no)
    return answer

## sorted 사용해서 정렬 후 값 비교 >> 효율성 up
def solution(participant, completion):
    p_articipant = sorted(participant)
    c_ompletion = sorted(completion)
    for i in range(0,len(participant)-1):
        if p_articipant[i] != c_ompletion[i]:
            answer = p_articipant[i]
            break
        else :
            answer = p_articipant[-1]
    return answer


# 남의 풀이 보며 공부
## collections.counter 모듈

###코드
#### import collections # collections 모듈 불러오기
#### frequency = collections.Counter('간장공장공장장') # 모듈이름.함수이름()
#### print(frequency)
###출력
#### Counter({'장': 4, '공': 2, '간': 1})

import collections #Counter()라는 함수는 빈도를 구하는 동작을 수행
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
