"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(nums):
    def recurr(bitmask):
        if len(bitmask) == len(nums):
            val = sum([bitmask[k] * num for k, num in enumerate(nums)])
            if val % 360 == 0: return True
            return False
        else: return recurr(bitmask + [1]) or recurr(bitmask + [-1])
    return recurr([])


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = [int(raw_input()) for _ in iters()]
    if solve(n): print "YES"
    else: print "NO"
