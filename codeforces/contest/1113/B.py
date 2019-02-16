"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(n):
    n.sort()
    res = 0
    for x in xrange(1, 100):
        for i in reversed(xrange(1, len(n))):
            if n[i] % x == 0:
                before = n[0] + n[i]
                after = n[0] * x + n[i] / x
                res = min(res, after - before)
                break
    return sum(n) + res






if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    raw_input()
    n = stdin()
    print solve(n)
