"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(subs):
    subs.sort(key = lambda x: len(x[0]))
    s1, s2 = subs[-1][0], subs[-2][0]
    s1, s2 = s1[0] + s2, s2[0] + s1
    def check(string):
        res = [-1 for _ in subs]
        for i in xrange(0, len(subs), 2):
            j = i + 1
            i_prefix = subs[i][0] == string[:len(subs[i][0])]
            i_suffix = subs[i][0] == string[-len(subs[i][0]):] 
            j_prefix = subs[j][0] == string[:len(subs[j][0])]
            j_suffix = subs[j][0] == string[-len(subs[j][0]):] 
            if i_prefix and j_suffix: res[i], res[j] = 'P', 'S'
            elif i_suffix and j_prefix: res[i], res[j] = 'S', 'P'
            else: return False 
        return res
    c1, c2= check(s1), check(s2)
    c = c1 if c1 else c2
    res = [-1 for _ in subs]
    for i, index in enumerate(zip(*subs)[1]): res[index] = c[i]
    return joint('', res)

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    t = int(raw_input())
    subs = []
    for i in xrange(2*t - 2):
        s = raw_input()
        subs.append([s, i])
    print solve(subs)
