"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(k, nums, mask):
    fixed_sum = 0
    for i, num in enumerate(nums):
        if mask[i]:
            fixed_sum += num
            nums[i] = 0
    res = 0
    for i, num in enumerate(nums[:-1]):
        nums[i + 1] += nums[i]
        ans = nums[i + 1] - nums[max(0, i + 1 - k)]
        res = max(res, ans)
    return res + fixed_sum



if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    vals = stdin()
    mask = stdin()
    print solve(k, vals, mask)
