#람다함수로 간단하게 표현
def solution1(s):
    return s.lower().count('p') == s.lower().count('y')

#rough하고 직관적인 풀이
def solution2(s):
    answer = True
    p = 0
    y = 0
    for i in s:
        if (i=="p" or i=="P"):
            p +=1
        elif (i=="y" or i=="Y"):
            y +=1
    if (p != y):
        answer = False
    print('Hello Python')
    return answer

