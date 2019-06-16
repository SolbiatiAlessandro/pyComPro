"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(l, n):
    """
    7
    1234567
    left, right = 0, int(s)
    res = pow(10, 100000) + 7
    for sep in range(l):
        ss = int(s[sep])
        left = left * 10 + ss
        pp = pow(10, l - sep - 1)
        right -= ss * pp
        if right >= (pp / 10) and left > 0 and right > 0:
            #print "valid"
            #print left + right
            res = min(res, left + right)
    return res
    """
    s = str(n)
    mid = len(s) / 2
    first_right = -1
    first_left  = -1
    for i in range(mid, l)
        if s[sep] != '0'

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    l = int(raw_input())
    n = int(raw_input())
    print solve(l, n)
