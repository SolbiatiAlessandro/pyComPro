"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
from collections import Counter
def solve(nums):
    tot = sum(nums)
    s = sorted(nums)
    a, b = s[-1], s[-2]
    #print a,b
    res = []
    for i, num in enumerate(nums):
        left = tot - num
        if left % 2 == 0:
            if num != a and num != b and (left / 2 == a or left / 2 == b):
                res.append(i)
            elif num == a and (left / 2 == b):
                res.append(i)
            elif num == b and (left / 2 == a):
                res.append(i)

    print len(res)
    for x in res:
        print x + 1,
    return

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    nums= stdin()
    nums= stdin()
    r= solve(nums)
