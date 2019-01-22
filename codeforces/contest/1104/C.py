"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(string):
    vert = [(1, 1), (3 ,1)]
    hor  = [(1, 2), (2, 2), (3, 2), (4, 2)]
    res = []
    iv, ih = 0, 0
    for char in string:
        if char == '0':
            res += [vert[iv]]
            iv += 1
            iv = iv % len(vert)
        if char == '1':
            res += [hor[ih]]
            ih += 1
            ih = ih % len(hor)
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    s=raw_input()
    res =  solve(s)
    for x in res:
        print x[0], x[1]
