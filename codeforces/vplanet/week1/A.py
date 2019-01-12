"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(n, k, nums):
    i, res = 0, 0
    while i != len(nums) - 1:
        j = min(k, len(nums) - 1 - i)
        while nums[i + j] == '0': j -= 1
        if j == 0: return -1
        i += j
        res += 1
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    nums = raw_input()
    print solve(n ,k, nums)
