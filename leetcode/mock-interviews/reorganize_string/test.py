import solve2

s = solve2.Solution()
s = s.reorganizeString
from random import random as r
for _ in xrange(1000):
    strlen = int(r()*49 + 1)
    string = "".join([chr(int(r() * (122-97) + 97)) for x in xrange(strlen)])
    got = s(string)
    print string, got
    different = True
    for i, char in enumerate(got[:-1]):
        if got[i + 1] == char: different = False
    assert different





