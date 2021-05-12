
#함수 solution은 정수 x와 자연수 n을 입력 받아
#x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴합니다.
def solution(x, n):
    return list(range(x,x*(n+1),x))

def solution(x, n):
    return [x*i for i in range(1, n+1)]