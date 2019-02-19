"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def _binomial(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    """
    print n, k
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def solve(n, k):
    dp = {}
    def binomial(n, k):
        if n < 0 or k < 0: return 0
        if k == 0: return 1
        if n == k: return 1
        mem = dp.get((n, k))
        if mem is not None: return mem
        res = binomial(n - 1, k - 1) + binomial(n - 1, k)
        dp[(n,k)] = res
        return res
        
    res = 1
    curr = 10
    splits = 1
    while curr > 1:
        left =  n - (k * splits)
        curr = binomial(max(left, splits) + 1, min(left, splits))
        res += curr
        splits += 1
    return res% 1000000007


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    print solve(n ,k)
