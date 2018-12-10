"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(s):
    cumsum = [0 for _ in s]
    try:first_a = s.index('a')
    except ValueError: return 0
    cumsum[first_a], prev, found_b = 1, first_a, False
    for i in xrange(first_a + 1, len(cumsum)):
        if s[i] == 'a':
            if found_b:
                cumsum[i] = 2*cumsum[prev] + 1
            else:
                cumsum[i] = 2*cumsum[prev] - cumsum[prev - 1]
            prev, found_b = i, False
        else:
            cumsum[i] = cumsum[i - 1]
            if s[i] == 'b': found_b = True
    return cumsum[-1] % (1000000000 + 7)

        

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    print solve(n)
