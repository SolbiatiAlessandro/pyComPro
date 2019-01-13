"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(inp):
    memo = {}
    MAXPOS = len(inp) + 1
    def dp(i, pos):
        try:
            if memo.get((i, pos)): return memo[(i, pos)]
            res = -1
            if (i == 0 and pos > 0) or pos < 0: res = 0
            elif i == 0 and pos == 0: res = 1
            elif inp[i - 1] == 'f': res = dp(i - 1, pos - 1)
            elif inp[i - 1] == 's': res = sum([dp(i - 1, j) for j in xrange(pos, MAXPOS)])
            memo[(i, pos)] = res
            return res
        except IndexError as e:
            print i, pos
            quit(e.message)

    res = sum([dp(len(inp) - 1, j) for j in xrange(MAXPOS)]) 
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    inp = []
    for _ in iters():
        inp.append(raw_input())
    print solve(inp)
