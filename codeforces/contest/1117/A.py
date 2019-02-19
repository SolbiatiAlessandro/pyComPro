"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(n):
    m = max(n)
    res = 0
    count = 0
    for i in n:
        if i != m:
            res = max(res, count)
            count = 0
        else:
            count += 1
    return max(res, count)

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    raw_input()
    n = stdin()
    print solve(n)
