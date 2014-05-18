from itertools import combinations

a1 = set([1, 2, 3])
a2 = set([2, 4])
a3 = set([1, 2])
a4 = set([1, 3, 4])
l = [a1, a2, a3, a4]

b1 = set([1])
b2 = set([3, 1, 4])
b3 = set([4, 1])
b4 = set([2, 1])
l2 = [b1, b2, b3, b4]


def combinator(values):
    l = [(a, b) for a, b in combinations(values, 2) if len(a ^ b) == 1]
    print len(l)
    print l


combinator(l)
print "Sol: a1-a3"
print "====================="
combinator(l2)
print "Sol: b1-b4, b2-b3"
