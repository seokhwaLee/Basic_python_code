## 나의 풀이
def solution(n):
    answer = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            answer = answer + i
    answer = answer + n
    return answer

## 코드 요약하기
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])