"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(nums):
    res = 0
    nums.sort()
    for i in xrange(0, len(nums) - 1, 2):
        num = nums[i]
        res += nums[i+1] - num
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    t=stdin()
    nums = stdin()
    print solve(nums)
