import math
from operator import add


def solution(N):
    f = math.factorial(N)
    f_str = map(int, str(f))
    print f_str
    res = reduce(add, f_str)
    if res > 10000000:
        return -1
    return res

print solution(14)
print solution(20)
print solution(20000000)