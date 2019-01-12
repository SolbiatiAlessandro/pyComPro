"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

from collections import Counter
def solve(s):
    c  = Counter(s)
    more, less = c['('], c[')']
    char = '('
    if (more - less) != 2: return 0
    counts = []
    count = 0
    m1counts = 0
    m1index = None
    for i,cc in enumerate(s):
        if cc == char:
            count += 1
        else:
            count -= 1
        if count == -1:
            return 0
        counts.append(count)
    #print counts
    if counts[-1] != 2: return 0
    last_1_index = len(counts) - 1 - counts[::-1].index(1)
    res = 0
    for i in range(last_1_index + 1, len(counts)):
        if s[i] == char:
            res += 1
    return res
    

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    s=raw_input()
    s = raw_input()
    print solve(s)
