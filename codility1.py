def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

print factors(24)

def solution(N):
    res = set()
    # Es necesaria la raiz cuadrada
    for i in range(1, int(N**0.5)+1):
        divisor, modulo = divmod(N, i)
        if modulo == 0:
            res |= set([i, divisor])
    return res

print solution(2)
print solution(24)
print solution(147)
