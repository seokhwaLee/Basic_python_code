def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if i**(1/2)-int(i**(1/2))==0:
            answer -= i
        else :
            answer += i
    return answer

print(solution(13,17))