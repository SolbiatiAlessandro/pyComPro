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
    def size(a,b,c,d):
        for num in nums[b:d+1]:
            if any(num[a:c+1]):
                return -1
        return 2*(c-a+1) + 2*(d-b+1)
    res = 4
    for height in xrange(n):
        for width in xrange(k):
            for x in xrange(k - width):
                for y in xrange(n - height): 
                    s = size(x, y, x+width, y+height)
                    res = max(res, s)
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    nums = []
    for _ in xrange(n):
        nums.append(raw_input())
    print solve(n ,k, nums)
