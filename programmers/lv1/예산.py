def solution(d, budget):
    sum=0
    answer = 0
    d.sort()
    for i in range(0,len(d)):
        sum += d[i]
        if sum > budget:
            break
        answer += 1
        
    return answer


def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d :
        budget -= i
        if budget < 0 :
               break
        cnt += 1
    answer = cnt
    return answer