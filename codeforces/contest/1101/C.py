"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(segms):
    start, end = [], []
    for i, (s,e) in enumerate(segms):
        start.append((s,i))
        end.append((e,i))
    start.sort()
    end.sort()
    mask = 0
    i, j =0, 0
    res = -1
    ans = [1] * len(segms)
    for j in xrange(len(end)):
        while i<len(start) and start[i][0] <= end[j][0]:
            mask |= (1<<start[i][1])
            i += 1
        mask &= (~(1<<end[j][1]))
        ans[end[j][1]] = 2
        if mask == 0 and j != len(end)-1:
            ans[end[j][1]] = 2
            res = j
            break
    if res == -1:
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
