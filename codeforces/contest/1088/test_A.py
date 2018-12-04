import A
for x in xrange(1, 101):
    got = A.solve(x)
    if got != -1:
        ok = True
        a, b = got[0], got[1]
        if not (1 <= a <= x and 1<= b <= x): ok = False
        if not (a % b == 0): ok =  False
        if not (a * b > x): ok = False
        if not (a / b < x): ok = False
        if not ok: print "#######"+str(x)

