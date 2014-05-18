from itertools import combinations


def represent_subset(S, L):
    l = [subset for subset in combinations(S, L)]
    print len(l)
    print l

represent_subset(range(1, 4), 2)