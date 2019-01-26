"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(s, w):
    s = s + "2"
    p = ""
    count = 0
    for i, char in enumerate(s[1:]):
        if s[i] == char: count += 1
        else:
            p += str(count + 1) 
            count = 0
    dp = {}
    def solve(seq):
        k = dp.get(seq)
        if k is not None:
            return k
        res = 0
        if len(seq) == 1:
            if seq[0] == "1": 
                res = w[0]
            else:
                val = int(seq[0])
                res = w[val - 1]
                for i in xrange((val)/2):
                    j = val - 2 - i
                    res = max(res, w[i] + w[j])
            dp[seq] = res
            return res
        if len(seq) == 2:
            res = solve(seq[0]) + solve(seq[1])
            dp[seq] = res
            return res
        for i in xrange(1, len(seq) - 1):
            sseq = seq[:i - 1] + str(int(seq[i - 1])+int(seq[i + 1])) + seq[i + 2:]
            local = solve(seq[i]) + solve(sseq) 
            res = max(local, res)
        dp[seq] = res
        return res
    res =  solve(p)
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    raw_input()
    s = raw_input()
    w = stdin()
    print solve(s, w)
