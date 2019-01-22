"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(n):
    if n < 10: return [n]
    for i in xrange(1, 11):
        if n % i == 0:
            res = []
            for k in xrange(n/i + 1): res.append(i)
            return res
    res = []
    for _ in xrange(0, n/9):
        res.append(9)
    res.append(n%9)
    return res
    

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = int(raw_input())
    res =  solve(n)
    for x in res: print x,
