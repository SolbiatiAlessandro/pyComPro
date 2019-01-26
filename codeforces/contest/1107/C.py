"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(n, k,nums,seq):
    count = 0
    sseq = []
    seq = seq+'*'
    res = 0
    for i, char in enumerate(seq[1:]):
        sseq.append(nums[i])
        if seq[i] == char:
            count += 1
        else:
            if count < k:
                res += sum(sseq)
            else:
                sseq.sort()
                res += sum(sseq[-k:])
            count = 0
            sseq = []
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    nums = stdin()
    seq = raw_input()
    print solve(n,k,nums,seq)
