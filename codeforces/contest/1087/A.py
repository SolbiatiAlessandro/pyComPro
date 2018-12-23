"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(s):
    res = ""
    if len(s) % 2 == 0:
        while True:
            if len(s) > 0:
                res += s[-1]
                s = s[:-1]
            if len(s) > 0:
                res += s[0]
                s = s[1:]
            if len(s) == 0: return res[::-1]
    else:
        while True:
            if len(s) > 0:
                res += s[0]
                s = s[1:]
            if len(s) > 0:
                res += s[-1]
                s = s[:-1]
            if len(s) == 0: return res[::-1]

    

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    print solve(n)
