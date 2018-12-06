"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)

def solve(n, k, a):
    res, a = [], [0] + sorted(list(set(a)))
    for i in xrange(min(len(a) - 1, k)): res.append(a[i + 1] - a[i])
    return res + [0] * (k - len(a) + 1)


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    a = stdin()
    got = solve(n, k, a)
    #import pdb;pdb.set_trace()
    for k in got:
        print k
