import C

def increase(a):
    stop = True
    for i, x in enumerate(a[:-1]):
        if a[i + 1] <= x:
            print i
            stop = False
    return stop

got = C.solve(3, [1,2,3])
assert increase(got)
got = C.solve(2000, [2000 - i for i in xrange(2000)])
print got
assert increase(got)
got = C.solve(3, [7,6,3])
print got
assert increase(got)
got = C.solve(3, [7,7,3])
print got
assert increase(got)

