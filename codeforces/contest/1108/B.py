"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(nums):
    big = max(nums)
    x = big
    from collections import Counter
    c = Counter(nums)
    y = 1
    for num in nums:
        if num > y and c[num] == 2:
            y = num
    for num in nums:
        if num > y and big % num != 0:
            y = num
    return x, y


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    raw_input()
    nums = stdin()
    res = solve(nums)
    for x in res: print x,
