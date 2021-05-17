
def solution(array, commands):
    answer = []
    # commands에 있는 요소들을 변수에 할당 (i, j, k)
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice = array[i-1:j] # array에서 슬라이스
        slice.sort() # 정렬
        answer.append(slice[k-1]) # 인덱싱
    return answer

## 코드 보며 람다함수 연습
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    #람다함수에서는 for 대신 map써서 반복문