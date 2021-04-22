##for,if문 사용해서 김서방찾기
def solution(seoul):
    x = 0
    for i in seoul:
        if i == 'Kim':
            break
        x = x+1

    answer = "김서방은 " + str(x) + "에 있다"
    return answer

seoul = ['Park', 'Kim',"Lee"]
where = solution(seoul)
print(where)

##index,format함수 이용해서 김서방 찾기
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
print(findKim(["Park","Lee","Kim"]))


##index 이용해서 김서방 찾기
def solution(seoul):
    return ('김서방은 %d에 있다' %seoul.index('Kim'))
