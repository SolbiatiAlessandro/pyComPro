"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(vals):
    res = 0
    for i, _ in enumerate(vals[:-2]):
        if vals[i] == 1 and vals[i + 1] == 0 and vals[i + 2] == 1:
            vals[i + 2] = 0
            res += 1
    return res



if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    t = raw_input()
    vals = stdin()
    print solve(vals)
