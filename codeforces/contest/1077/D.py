"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
from collections import Counter
def solve(n, k, nums):
    occurs = Counter(nums)
    def max_len(times):
        res = 0
        for v in occurs.values():
            res += v / times
        return res

    """a, b = 0, 100007
    while b > a:
        m = (b - a)/2 + a
        r1 = max_len(m)
        r2 = max_len(m)
        if r1 >= k and r2 < k: return m
        if r > k: a = m
        if r < k: b"""

    i = 1
    while True:
        r = max_len(i)
        if r < k:
            break
        i+=1

    res = []
    for num, v in occurs.items():
        if k == 0:
            break
        t = v / (i - 1)
        res += [num] * t
        k -= t

    print joint(' ', res)  

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    nums = stdin()
    r= solve(n ,k, nums)
