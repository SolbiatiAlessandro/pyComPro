"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(n):
    res = n/7
    if n%7: return res + 1
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    for _ in xrange(int(n)):
        x = raw_input()
        print solve(int(x))
