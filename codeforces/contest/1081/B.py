"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
from collections import Counter
def solve(nums):
    n = len(nums)
    c = Counter(nums)
    #import pdb;pdb.set_trace()
    for k, v in c.items():
        if v % (n - k) != 0:
            print "Impossible"
            return -1
    print "Possible"
    nums = sorted([(num, i) for i, num in enumerate(nums)])
    res = {}
    counter = 0
    letter = 1
    #import pdb;pdb.set_trace()
    for num, i in nums:
        size = n - num
        res[i] = letter
        if counter == size - 1: 
            letter += 1
            counter = 0
        else:
            counter += 1
    list_res = ['' for _ in xrange(n)]
    for i, _ in enumerate(list_res):
        list_res[i] = str(res[i])
    r = ' '.join(list_res)
    print r
    return 

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    nums = map(int, raw_input().split())
    solve(nums)
