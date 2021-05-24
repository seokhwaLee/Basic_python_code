def solution(s):
    if len(s) == 4 or len(s)==6:
        try:
            int(s)
            answer = True
        except:
            answer = False
    else :
        answer = False
    return answer


#코드 공부
##isalpha함수는 문자열이 문자인지 아닌지를 True,False로 리턴 
##isdigit함수는 문자열이 숫자인지 아닌지를 True,False로 리턴
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)