from operator import add


def solution(A, B):
    count = 0
    for x in range(A, B + 1):
        x_str = map(int, str(x))
        res = reduce(add, x_str)
        # Sin operator => res = reduce(lambda x, y: x+y, x_str)
        if res / float(len(x_str)) > 7:
            count += 1

    return count


print solution(8675, 8689)