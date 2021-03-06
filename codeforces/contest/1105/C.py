"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(n, l, r):
    l, m = l - 1, pow(10, 9) + 7
    dp = [[r/3 - l/3, (r + 2)/3 - (l + 2)/3, (r + 1)/3 - (l + 1)/3]]
    last = dp[0]
    for i in range(n - 1):
        a = last[0]*dp[0][0] + last[2]*dp[0][1] + last[1]*dp[0][2]
        b = last[0]*dp[0][1] + last[1]*dp[0][0] + last[2]*dp[0][2]
        c = last[1]*dp[0][1] + last[2]*dp[0][0] + last[0]*dp[0][2]
        last = [a%m,b%m,c%m]
    return last[0]

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, l, r = stdin()
    print solve(n, l, r)
