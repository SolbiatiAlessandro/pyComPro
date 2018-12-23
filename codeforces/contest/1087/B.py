"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

from operator import truediv
from math import ceil
def solve(n, k):
    res = 1e9
    #import pdb;pdb.set_trace()
    for i in xrange(1, k):
        if n % (k - i) == 0:
             temp = int((n / (k - i)) * k + (k - i))
             res = min(res, temp)
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    print solve(n ,k)
