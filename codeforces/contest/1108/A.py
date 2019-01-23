"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(l1,r1,l2,r2):
    if l1 != r2: print l1, r2
    elif r1 != r2: print r1, r2
    elif l1 != l2: print l1, l2
    elif r1 != l2: print r1, l2

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    for _ in iters():
        l1,r1,l2,r2 = stdin()
        solve(l1,r1,l2,r2)
