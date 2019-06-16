"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(x, y, p):
    r1 = x % p
    r2 = y % p
    c = (x/p) + (y/p)
    if r1 + r2 >= p:
        return c + 1, p - max(r1, r2)
    return c, 0

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k, u = stdin()
    res= solve(n , k , u)
    for x in res: print x,
