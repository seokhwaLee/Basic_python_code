## 모래시계 출력하기
cnt = 0
height = int(input('높이를 입력하세요 : '))
while cnt < height:
    cnt = cnt+1
    print((' ')*((cnt-1)+1) + '*'*(height*2-cnt*2+1))

cnt=0
while cnt < int(height)-1:
     cnt = cnt+1
     print((' ')*(height-cnt) + '*' * (1+cnt*2))