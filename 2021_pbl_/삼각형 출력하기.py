## 삼각형 출력하기
cnt = 0
height = input('높이를 입력하세요 : ')

while cnt < int(height):
    cnt = cnt+1
    star = cnt - 1
    print((' ')*(int(height)-cnt) + '*' * (1+(cnt-1)*2))