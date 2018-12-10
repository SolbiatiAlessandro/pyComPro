"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(A):
    res = 1e9
    for x in xrange(1, 101):
        _res = 0 
        for i, num in enumerate(A):
            index = i + 1
            value = 2*(x-1 + index-1 + abs(x - index))
            _res += num * value
        res = min(res, _res)
        #print x, _res
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = stdin()
    A = stdin()
    print solve(A)
