"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(vals):
    i = 0
    res = 0
    vals = joint('', vals)
    #import pdb;pdb.set_trace()
    while i < len(vals):
        found =  vals[i:].find("101")
        if found == -1: return res
        i +=  found
        j = 0
        count = 0
        while j == 0:
            count += 1
            i += 2
            j = vals[i:].find("101")
        res += (count + 1) / 2
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    t = raw_input()
    vals = stdin()
    print solve(vals)
