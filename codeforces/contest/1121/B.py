"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(nums):
    snums = set(nums)
    nums.sort()
    res = 0
    for s in xrange(nums[0] + nums[1], nums[-1] + nums[-2] + 1):
        lres = 0
        for num in nums:
            if (s - num) in snums: lres += 1
        res = max(lres/2, res)
    return res


    

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    raw_input()
    nums = stdin()
    print solve(nums)
