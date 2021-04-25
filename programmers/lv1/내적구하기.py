a = [1,2,3,4]
b = [-3,-1,0,2]
#함수 사용해서 내적 구하기
def solution(a,b):
    ans = 0
    for i in range(len(a)):
        ans = a[i]*b[i]+ans
    return ans

# 함수 단순화
def solution(a,b):
    return sum([a[i]*b[i] for i in range(len(a))])

# int사용해서 내적 구하기
int solution(int a[], size_t a_len, int b[], size_t b_len) {
    int answer = 0;
    int i;

    for(i=0;i<a_len;i++)
        answer += a[i]*b[i];   

    return answer;
}
