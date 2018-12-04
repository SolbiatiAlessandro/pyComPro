x = int(raw_input())
def solve(x):
    for b in xrange(1, x + 1):
        for a in xrange(1, x + 1):
            ok = True
            if not (a % b == 0): ok =  False
            if not (a * b > x): ok = False
            if not (a / b < x): ok = False
            if ok:
                return a, b
    return -1
got = solve(x)
print got if type(got) is int else "{} {}".format(got[0], got[1])
