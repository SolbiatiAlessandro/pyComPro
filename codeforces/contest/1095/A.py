"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(s):
    i = 0
    k = 1
    res = ""
    while i < len(s):
        res += s[i]
        i += k
        k += 1
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    s = raw_input()
    print solve(s)
