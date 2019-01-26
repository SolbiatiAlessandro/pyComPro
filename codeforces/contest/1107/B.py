"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(n, k):
    return (9 * (n-1)) + k

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    for _ in iters():
        n, k = stdin()
        print solve(n ,k)
