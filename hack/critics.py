from itertools import combinations

C, N = raw_input().split(" ")
d = []
for row in range(1, int(N) + 1):
    d.append(set([int(x) for x in raw_input().split(" ")]))

l = [(d.index(a) + 1, d.index(b) + 1) for a, b in combinations(d, 2) if len(a ^ b) == 1]
if len(l) > 1:
    l1 = []
    for a, b in combinations(l, 2):
        if len(set(a) & set(b)) == 0:
            l1.append(a)
            l1.append(b)
else:
    l1 = l

print len(l1)
for i in range(len(l1)):
    print "{0} {1}".format(l1[i][0], l1[i][1])


    # def combinator(values):
    #     l = [(a, b) for a, b in combinations(values.values(), 2) if len(a ^ b) == 1]
    #     print len(l)
    #     print l
    #
    # combinator(d)

    # a1 = set([1, 2, 3])
    # a2 = set([2, 4])
    # a3 = set([1, 2])
    # a4 = set([1, 3, 4])
    # l = [a1, a2, a3, a4]
    #
    # b1 = set([1])
    # b2 = set([3, 1, 4])
    # b3 = set([4, 1])
    # b4 = set([2, 1])
    # l2 = [b1, b2, b3, b4]

    # combinator(l)
    # print "Sol: a1-a3"
    # print "====================="
    # combinator(l2)
    # print "Sol: b1-b4, b2-b3"
