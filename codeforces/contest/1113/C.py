"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

from operator import xor
def complete_search(n, verbose = True):
    res = 0
    le = len(n)
    for r in xrange(1, le+1):
        for l in xrange(1, le+1):
            if l <= r and (r - l + 1) % 2 == 0:
                mid = (l+r-1)/2
                left = [n[i] for i in xrange(l - 1, mid)]
                right = [n[i] for i in xrange(mid, r)]
                eq = reduce(xor, left) == reduce(xor, right)
                res += eq
                if eq and verbose: print n[l - 1: r]
    return res

res = [0]

def solve(n):
    memo = {}
    def recurr(i, j):
        if i == j: return n[i]
        val = memo.get((i, j))
        if val is not None: return val
        elif (j - i) % 2 != 0:
            mid = (j + i - 1)/2
            lo = recurr(i, mid) == recurr(mid + 1, j)
            res[0] += lo
            lres = recurr(i, mid) ^ recurr(mid + 1, j)
            recurr(i, j-1)
            recurr(i+1, j)
        else:
            mid = (j + i - 1)/2
            lres = recurr(i, mid) ^ recurr(mid + 1, j)
            recurr(i, j-1)
            recurr(i+1, j)
        memo[(i, j)] = lres
        return lres
    recurr(0, len(n) - 1)
    if len(n) > 1: recurr(0, len(n) - 2) 
    recurr(1, len(n) - 1)
    return res[0]


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    raw_input()
    n = stdin()
    #print complete_search(n)
    print solve(n)

