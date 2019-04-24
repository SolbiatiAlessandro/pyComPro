"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(a, b):
    #import fractions
    """
    for m in range(0,20):
        print a+m,b+m
        print(fractions.gcd(a+m, b+m))
    """
    if a == 1 or b == 1: return 0
    d = abs(a - b)
    if d == 0: return 0
    if min(a, b) % d == 0: return 0
    k = min(a, b) / d
    #print d, k 
    return (d * (k + 1)) - min(a, b)



if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    print solve(n ,k)
