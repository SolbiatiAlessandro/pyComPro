"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(n, k, nums):
    for i, num in enumerate(nums):
        nums[i] = map(int,list(num))
    dp = [[[[1 for _ in xrange(n)] for __ in xrange(k)] \
            for ___ in xrange(n)] for ____ in xrange(k)]
    def size(a,b,c,d):
        if c == 0 or d == 0: return nums[d][c] == "1"
        if not dp[a][b][c-1][d] and\
           not dp[a][b][c][d-1] and\
           nums[d][c] == "0": return 0
        else: return 1

    res = 4
    for height in xrange(n):
        for width in xrange(k):
            for x in xrange(k - width):
                for y in xrange(n - height): 
                    a,b,c,d = x, y, x+width, y+height
                    dp[a][b][c][d] = size(a,b,c,d)
                    if dp[a][b][c][d] == 0:
                        res = max(res, (c+1-a)*2+(d+1-b)*2)
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    nums = []
    for _ in xrange(n):
        nums.append(raw_input())
    print solve(n ,k, nums)
