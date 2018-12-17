"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
from collections import Counter
from collections import defaultdict
def solve(nums):
    groups = defaultdict(list)
    for i, num in enumerate(nums):
        groups[len(nums) - num].append(i)

    kind = 0
    for group, indexes in groups.items():
        if len(indexes) % group != 0:
            print "Impossible"
            return -1
        for i in xrange(0, len(indexes), group):
            kind += 1
            for j in xrange(group):
                nums[indexes[i + j]] = kind
    print "Possible"
    print joint(" ",nums)
    return nums


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = stdin()
    nums = stdin()
    r = solve(nums)
