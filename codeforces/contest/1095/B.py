"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(nums):
    big, small = max(nums), min(nums)
    nums1, nums2 = nums[:], nums[:]
    del nums1[nums1.index(big)]
    del nums2[nums2.index(small)]
    #print nums1, big
    #print nums2, small
    return min(max(nums1) - min(nums1), max(nums2) - min(nums2))


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = stdin()
    nums = stdin()
    print solve(nums)
