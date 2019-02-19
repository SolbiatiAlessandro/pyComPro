"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(n,a,b):
    price = min(2 * a, b)
    two = n / 2
    one = n % 2
    return price * two + a * one
    

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    for _ in iters():
        n, a, b = stdin()
        print solve(n, a, b)
