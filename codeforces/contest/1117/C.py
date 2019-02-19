"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(x1,y1,x2,y2,s):
    n = len(s)
    wind = []
    currx = 0
    curry = 0
    for d in s:
        if d =="U": curry += 1
        if d =="D": curry -= 1
        if d =="R": currx += 1
        if d =="L": currx -= 1
        wind.append([currx, curry])

    def search(days, verbose=False):
        if verbose:print("called search "+str(days))
        wlocA =  wind[n - 1]
        wlocB = wind[(days % n) - 1] if (days % n) > 0 else [0, 0]
        wloc = [(days / n) * wlocA[0] + wlocB[0],(days / n) * wlocA[1] + wlocB[1]]

        target = [x2 - x1, y2 - y1]
        missing = abs(target[0] - wloc[0]) + abs(target[1] - wloc[1])
        if verbose:print days, wloc, target, missing
        return missing <= days

    if not search(pow(10, 18)): return -1
    a, b = 0, 2 * pow(10, 18)
    while b > a:
        index = (b - a)/2 + a
        before = search(index - 1) if index > 0 else False
        curr = search(index)
        #print("index {} {}: before {}, curr {}".format(a, b, before,curr))
        if not before and curr: return index
        if before and curr: b = index 
        elif not before and not curr: a = index 
        else:
            print b,a
            print before
            print curr
            exit("problem")


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    x1,y1 = stdin()
    x2,y2 = stdin()
    n = raw_input()
    s = raw_input()
    print solve(x1,y1,x2,y2,s)
