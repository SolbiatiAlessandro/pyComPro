"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(c, k):
    cp,cd=0,0
    for n in c:
        if n % 2 == 0:
            cp += 1
        else:
            cd += 1
    kp,kd=0,0
    for n in k:
        if n % 2 == 0:
            kp += 1
        else:
            kd += 1
    return min(cp,kd) + min(cd,kp)

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    c = stdin()
    k = stdin()
    print solve(c,k)
