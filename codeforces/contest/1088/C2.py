"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(nums):
    added = 0
    res = []
    print len(nums) + 1
    for i in xrange(len(nums)):
        index = len(nums) - i - 1
        num = nums[index] + added
        curr = num % len(nums)
        target = index if index >= curr else index + len(nums)
        added += (target - curr)
        res.append((nums[index] + added) % len(nums))
        print "1 {} {}".format(index + 1, target - curr)
    print "2 {} {}".format(len(nums), len(nums))
    return res[::-1]
    

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = stdin()
    A = stdin()
    solve(A)
