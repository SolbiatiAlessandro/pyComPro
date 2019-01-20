"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(nums):
    res, tres = 1e9, -1
    for t in xrange(1, 101):
        cost = 0
        for num in nums:
            if num < t:
                cost += t - 1 - num
            elif num > t:
                cost += num - 1 - t
        if cost < res:
            res = cost
            tres = t
    return tres, res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    n = stdin()
    res =  solve(n)
    for x in res: print x,
