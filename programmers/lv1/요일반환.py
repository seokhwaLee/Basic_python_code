#2016년의 요일을 반환하는 함수 만들기
def solution(a, b):
    lista=['SUN','MON','TUE','WED','THU','FRI','SAT']
    if a==1 or a==4 or a==7:
        answer=lista[(b+4)%7]
    elif a==2 or a==8:
        answer=lista[b%7]
    elif a==3 or a==11:
        answer=lista[(b+1)%7]
    elif a==5:
        answer=lista[(b+6)%7]
    elif a==6:
        answer=lista[(b+2)%7]
    elif a==9 or a==12:
        answer=lista[(b+3)%7]
    elif a==10:
        answer=lista[(b+5)%7]
    return answer
print(solution(2,24))


from datetime import date
DAY = {0: 'MON', 1: 'TUE', 2: 'WED', 3: 'THU', 4: 'FRI', 5: 'SAT', 6: 'SUN'}
def getDayName(a,b):
    d = date(2016, a, b)
    return DAY[d.weekday()]
print(getDayName(2,24))


def getDN(a,b):
    week=['FRI','SAT','SUN','MON','TUE','WED','THU']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    return week[(sum(month[:a-1])+(b-1))%7]
print(getDN(2,24))