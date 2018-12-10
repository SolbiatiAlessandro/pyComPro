"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(n, target, A):
    if sum(A) < target: return -1
    if sum(A) == target: return 0
    res = min(A)
    for x in A:
        target -= (x - res)
    if target < 0: return res
    from operator import truediv
    from math import ceil
    return res - int(ceil(truediv(target, len(A))))

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, t = stdin()
    A = stdin()
    print solve(n, t, A)
