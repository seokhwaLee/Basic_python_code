# 글자 수만큼 수박나타내기 ex) 수, 수박, 수박수
def solution(n):
    tnqkr = ['수','박']
    answer = '수박'*(n//2) + '수'*(n%2)
    return answer


def water_melon(m):
    wm = '수박'*(m//2+1)
    return wm[:m]


# for i in range(l)을 사용해서 ['수','박']리스트를 이용해
# 홀일땐 수, 짝일땐 박 넣기
def WM(l):
    return "".join(['수박'[i%2] for i in range(l)])


print(solution(4), water_melon(5), WM(6))