"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(_segms):
    segms = []
    for i, s in enumerate(_segms):
        segms.append((s,i))
    segms.sort()
    big = segms[0][0][1]
    ans = [1] * len(segms)
    res = 0
    for i,seg in enumerate(segms):
        if segms[i][0][0] > big:
            res = 1
            break
        ans[segms[i][1]] = 2
        big = max(big, segms[i][0][1])
    if not res:
        print -1
        return []
    return ans

    
if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    for _ in iters():
        segms = []
        for __ in iters():
            a,b =stdin()
            segms.append((a,b))
        got = solve(segms)
        if got: print joint(" ",got) 
