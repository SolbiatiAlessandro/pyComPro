"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(n, k, nums):
    dp = [1e9 for _ in nums]
    dp[0] = 0
    for i, num in enumerate(nums):
        if num == "1":
            for j in xrange(1, k + 1): dp[i] = min(dp[i], 1 + dp[i - j])
    return dp[-1] if dp[-1] != 1e9 else -1


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    nums = raw_input()
    print solve(n ,k, nums)
