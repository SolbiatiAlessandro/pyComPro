"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(s):
    prev = 0
    for i, c in enumerate(s):
        if ord(c) < prev:
            return i-1, i
        prev = ord(c)
    return None, None

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = stdin()
    s = raw_input()
    a,b= solve(s)
    if a is None:
        print "NO"
    else:
        print "YES"
        print a, b
