"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return range(int(input()))


def solve(s):
    n = len(s)
    memo = [[-1 for _ in range(n)] for _ in range(n)]
    def dp(l, r):
        if l > r: return 0
        if memo[l][r] != -1: return memo[l][r]
        res = min([1 + dp(l + 1, r)] +                    \
                [dp(l + 1, i - 1) + dp(i, r) for          \
                i in range(l + 1, r + 1) if s[i] == s[l]])
        memo[l][r] = res
        return res
    return dp(0, n - 1)


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    _,s=input(),input()
    print(solve(s))
