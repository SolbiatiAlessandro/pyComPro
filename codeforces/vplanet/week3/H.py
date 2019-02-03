"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(n, W, B, X):
    memo = {}
    def dp(i, mana, capacity):


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, W, B, X = stdin()
    quantities = stdin()
    costs = stdin()
    print solve(n, W, B, X,quantities,costs)
