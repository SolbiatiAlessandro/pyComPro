"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(b):
    a = [0 for _ in b] + b[::-1]
    m, M = 0, a[-1]
    #import pdb;pdb.set_trace()
    for i in xrange(len(b)):
        right, left = len(a)-1-i, i
        target = a[right]
        a[left] = m
        a[right] = M
        if m + M > target:
            a[right] -= (m + M) - target
        elif m + M < target:
            a[left] += target - (m + M)
        m = a[left]
        M = a[right]
    return a


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = stdin()
    nums = stdin()
    res = solve(nums)
    out = ""
    for x in res: out += str(x)+" "
    print out[:-1]
