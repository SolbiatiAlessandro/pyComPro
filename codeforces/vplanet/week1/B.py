"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(n, k, nums):
    def side(nums):
        prev = -1
        res  = 0
        height = 1
        for num in nums:
            try: curr = num.index('1')
            except: curr = len(num)
            if prev == curr: height += 1
            else: curr_sum = 1
            res = max(res, curr*2 + height*2)
            prev = curr
        return res
    res = side(nums)
    for i, num in enumerate(nums): nums[i] = num[::-1]
    res = max(res, side(nums))
    nums = zip(*[list(num) for num in nums])
    res = max(res, side(nums))
    for i, num in enumerate(nums): nums[i] = num[::-1]
    res = max(res, side(nums))
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    nums = []
    for _ in xrange(n):
        nums.append(raw_input())
    print solve(n ,k, nums)
