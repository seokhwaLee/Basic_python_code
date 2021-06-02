import numpy as np
def solution(n):
    array1 = np.array(range(1,7071069))
    array1 = array1**2
    if n in array1:
        answer = (n**(1/2)+1)**2
    else :
        answer = -1
    return answer

def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'

import math
def nextSqure(n):
    return 'no' if not math.sqrt(n).is_integer() else (math.sqrt(n)+1)**2

def nextSqure(n):
    sqrt = pow(n, 0.5)
    return pow(sqrt + 1, 2) if sqrt == int(sqrt) else 'no'