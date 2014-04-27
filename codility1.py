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
        print "i:{}".format(i)
        divisor, modulo = divmod(N, i)
        print "div: {0}, mod:{1}".format(divisor, modulo)
        if modulo == 0:
            res = res.union({i, divisor})
    return res

print solution(2)
print solution(24)
print solution(147)