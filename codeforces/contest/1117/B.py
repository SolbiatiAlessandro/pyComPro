"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(m,k,a):
    big1, big2 = 0, 0
    for e in a:
        if e > big2:
            big2 = e
            if big2 > big1:
                big1, big2 = big2, big1
    times = m / (k + 1)
    res = (big1 * k + big2) * times
    left = m - ((k + 1) * times)
    return res + (left * big1)

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, m,  k = stdin()
    a = stdin()
    print solve(m,k,a)
