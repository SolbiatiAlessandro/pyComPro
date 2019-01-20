"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(_, k, string):
    res = 0
    for i in xrange(ord('a'), ord('z') + 1):
        #import pdb;pdb.set_trace()
        letter = chr(i)
        target = letter * k
        cnt = 0

        index = 0
        while index < len(string):
            if string[index] == letter:
                index += 1
                c = 1
                while index < len(string) and string[index] == letter and c < k:
                    index += 1
                    c += 1
                if c == k: cnt += 1
            else: index += 1
        """
        f = string.find(target)
        index = k + f
        while f != -1:
            cnt += 1
            f = string[index:].find(target)
            index += (k + f)
        """
        res = max(res, cnt)
    return res
        

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    string = raw_input()
    print solve(n ,k, string)
