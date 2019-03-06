"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(n, painters):
    res = 0
    fence = [[] for _ in xrange(n)]
    for p, (s, e) in enumerate(painters):
        for i in xrange(s - 1, e):
            if len(fence[i]) == 2: fence[i][0] = '*'
            if not fence[i] or fence[i][0] != '*':
                fence[i].append(p)

    single = [0 for _ in xrange(len(painters))]
    intersection = [single[::] for _ in xrange(len(painters))]
    for p, (s, e) in enumerate(painters):
        for i in xrange(s - 1, e):
            if len(fence[i]) == 1:
                single[p] += 1
            elif fence[i][0] != '*':
                other = fence[i][0]
                if other == p: other = fence[i][1]
                intersection[p][other] += 1
    q = len(painters)
    tot = sum([1 for x in fence if x])
    res = 0
    for i in xrange(q):
        for j in xrange(i + 1, q):
            ans = single[i] + single[j] + intersection[i][j]
            res = max(res, tot - ans)

    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, q = stdin()
    import sys
    lines = sys.stdin.readlines()
    painters = []
    for i in xrange(q):
        painters.append(map(int, lines[i].split(' ')))
    print solve(n, painters)
