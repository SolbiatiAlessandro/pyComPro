"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(A, s, f):
    size = f - s - 1
    l = len(A)
    A = [0] + A + A
    for i, _ in enumerate(A[:-1]): A[i + 1] += A[i]
    res, local_max = 1e9, -1
    get_res = lambda res: ( ( s - 1 - res) % l ) + 1
    for i in xrange(l):
        local_ans = A[i + size + 1] - A[i] 
        local_res = get_res(i)
        if local_ans > local_max or (local_ans == local_max and local_res < res):
            local_max = local_ans
            res = local_res
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    A = stdin()
    s, f = stdin()
    print solve(A, s, f)
