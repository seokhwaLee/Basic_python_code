##나의 풀이
def average(list):
    return (sum(list) / len(list))


#numpy모듈
import numpy
def solution(arr):
    answer = numpy.mean(arr)
    return answer

#코드 학습
#reduce()함수, 람다함수 공부
from functools import reduce
def average(list):
    return reduce(lambda x, y : x + y, list) / len(list)
##reduce(집계 함수, 순회 가능한 데이터[, 초기값])
###파이썬의 functools 내장 모듈의 reduce() 함수는 여러 개의 데이터를 대상으로 누적 집계를 내기 위해서 사용
###초기값을 기준으로 데이터를 루프 돌면서 집계 함수를 계속해서 적용하면서 데이터를 누적하는 방식으로 작동

##lambda
###x+y함수 람다함수로 표현(lambda x,y: x + y)
###x=10,y=20일 때 (lambda x,y: x + y)(10, 20)