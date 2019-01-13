"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(inp):
    memo = {} # memo table for the main dp recursion
    memo_sum = {} # memo table for the suffix sum used for speed up
    MAXPOS = len(inp) + 1

    def suffix_sum(i, pos):
        # res = sum([dp(i, j) for j in xrange(pos, MAXPOS)])
        if memo_sum.get(i):
            i_sum = memo_sum[i]
        else:
            i_sum = [dp(i, j) for j in xrange(MAXPOS)]
            for i in reversed(xrange(len(i_sum) - 1)): i_sum[i] += i_sum[i + 1]
            memo_sum[i] = i_sum
        return i_sum[pos]

    def dp(i, pos):
        try:
            if memo.get((i, pos)): return memo[(i, pos)]
            res = -1
            if  (i == 0 and pos > 0) or pos < 0: res = 0
            elif i == 0 and pos == 0: res = 1
            elif inp[i - 1] == 'f': res = dp(i - 1, pos - 1)
            elif inp[i - 1] == 's':
                res = suffix_sum(i - 1, pos)
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
