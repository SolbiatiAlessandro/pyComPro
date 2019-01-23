"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(string):
    l = len(string) / 3 + 1
    counters = [0 for _ in xrange(6)]
    strs = [
    "RGB" * l,
    "RBG" * l,
    "GBR" * l,
    "GRB" * l,
    "BRG" * l,
    "BGR" * l
    ]
    for i, c in enumerate(string):
        for ci in xrange(6):
            if c != strs[ci][i]: counters[ci] += 1
    m = min(counters)
    print m
    for ci in xrange(6):
        if m == counters[ci]: return strs[ci][:len(string)]


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    n = raw_input()
    print solve(n)
