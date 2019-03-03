"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(n,m,k,pows,schools,c):
    maxs = [0 for _ in xrange(m)]
    for i in xrange(n):
        maxs[schools[i] - 1] = max(maxs[schools[i] - 1], pows[i])
    res = 0
    for i in c:
        p = pows[i - 1]
        s = schools[i - 1]
        if p < maxs[s - 1]: res += 1
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, m, k= stdin()
    pows = stdin()
    schools = stdin()
    c = stdin()
    print solve(n,m,k,pows,schools,c)
