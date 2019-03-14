"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(s):
    n = len(s)
    memo = [[-1 for _ in xrange(n)] for _ in xrange(n)]
    def dp(l, r):
        if l > r: return 0
        if memo[l][r] != -1: return memo[l][r]
        res = 1 + dp(l + 1, r)
        for i in xrange(l + 1, r + 1):
            if s[i] == s[l]:
                res = min(res, dp(l + 1, i - 1) + dp(i, r))
        memo[l][r] = res
        return res
    return dp(0, n - 1)


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    _,s=raw_input(),raw_input()
    print solve(s)
