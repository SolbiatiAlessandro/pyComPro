"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(read):
    x = (1 << 26) - 1
    for index, (sym, string) in enumerate(read):
        mask = 0
        for letter in set(string):
            mask |= 1 << (ord(letter) - ord('a'))
        if sym == '!': x &= mask
        else: x &= (~mask)

        bits_on = sum([1 for i in xrange(26) if ((1 << i) & x)])
        if bits_on == 1: break

    return sum([1 for sym, string in read[index + 1:-1] if sym == '!' or sym == '?'])


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    read = []
    for _ in iters():
        sym, string = stdin("str")
        read.append((sym, string))
    print solve(read)
