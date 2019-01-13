"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(n, k, nums):
    queue = [index for index in xrange(len(nums)) if nums[index] == "1"][::-1]
    print queue
    dp = [1e9 for _ in nums]
    dp[0] = 0
    for i, num in enumerate(nums):
        if nums[i] == "1":
            while queue[-1] < (i - k): queue.pop()
            dp[i] = 1 + dp[queue[-1]]
            # TODO: wrong answer
            print queue
    return dp[-1] if dp[-1] < 1e9 else -1


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    nums = raw_input()
    print solve(n ,k, nums)
