"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(a,b,c,d):
    if a != d: return 0
    if c > 0 and a < 1: return 0 
    return 1
    

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    a = int(raw_input())
    b = int(raw_input())
    c = int(raw_input())
    d = int(raw_input())
    print solve(a,b,c,d)
