from itertools import combinations


def represent_subset(S, L):
    l = [subset for subset in combinations(S, L)]
    print len(l)
    for item in l:
        print " ".join(str(item[i]) for i in range(len(item)))


S, L = raw_input().split(" ")
represent_subset(range(1, int(S) + 1), int(L))
