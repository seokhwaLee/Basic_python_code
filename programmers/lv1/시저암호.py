def solution(s, n):
    lista =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    answer=[]
    for i in s:
        if i == ' ':
            answer.append(i)
        elif i.islower():
            k=lista.index(i)
            answer.append(lista[k-26+n])
        else:
            k=lista.index(i.lower())
            answer.append(lista[k-26+n].upper())
    return ''.join(answer)

# 아스키코드 활용
## ord() : 특정한 한 문자를 아스키 코드 값으로 변환해주는 함수
## chr() : 아스키코드 값을 문자로 변환해주는 함수 (10진수, 16진수 사용 가능)
def solution(s, n):
    answer = ''
    for i in s :
        if i.isupper() :
            answer += chr(ord(i)+n) if ord(i)+n < 91  else chr(ord(i)-26+n)
        elif i.islower() :
            answer += chr(ord(i)+n) if ord(i)+n < 123  else chr(ord(i)-26+n)
        elif i == ' ' :
            answer += i
    return answer    