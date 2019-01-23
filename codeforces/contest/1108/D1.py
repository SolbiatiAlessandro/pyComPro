"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

from operator import __add__

def other(c1, c2):
    for c in ['G','B','R']:
        if c not in [c1, c2]: return c

def solve(string):
    letters = list(set(string))

    def block(start, end):
        for i in xrange(start, end + 1):
            if (i-start) % 2:
                res.append(other(string[start], string[end + 1]))
                resc[0] += 1
            else: res.append(string[start])

    res, resc, count = [], [0], 0
    string += '*'
    for i, char in enumerate(string[1:]):
        if char == string[i]: count += 1
        else:
            block(i - count, i)
            count = 0
    print resc[0]
    return ''.join(res)


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    n = raw_input()
    print solve(n)
