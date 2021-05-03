def solution(a,b):
    answer=0
    for i in range(a,b+1):
        answer += i
    if answer == 0:
        for i in range(b,a+1):
            answer += i
    return answer

def solution(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))