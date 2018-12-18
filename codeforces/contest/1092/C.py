"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(subs):
    #print subs
    #import pdb;pdb.set_trace()
    subs.sort(key = lambda x: len(x[0]))
    string1 = subs[-1][0] + subs[-2][0][-1]
    string2 = subs[-2][0] + subs[-1][0][-1]
    is1 = False
    if subs[-2][0] == string1[1:]: is1 = True
    string = string1 if is1 else string2
    #print string
    classes = [-1 for _ in subs]
    l = 1
    wrong = False
    for i in xrange(0, len(subs), 2):
        evaluate = subs[i][0]
        class_0 = evaluate == string[:l] #prefix
        if class_0:
            classes[i] = 0
            classes[i + 1] = 1
        elif evaluate != string[-l:]:
            #wront string
            wrong = True
            break
        else:
            classes[i] = 1
            classes[i + 1] = 0
        l += 1

    if wrong:
        is1 = not is1
        string = string1 if is1 else string2
        #print string
        classes = [-1 for _ in subs]
        l = 1
        wrong = False
        for i in xrange(0, len(subs), 2):
            evaluate = subs[i][0]
            class_0 = evaluate == string[:l] #prefix
            if class_0:
                classes[i] = 0
                classes[i + 1] = 1
            elif evaluate != string[-l:]:
                exit('no strings!')
            else:
                classes[i] = 1
                classes[i + 1] = 0
            l += 1
    
    res = ['' for _ in subs]
    for i, dd in enumerate(subs):
        index = dd[1]
        res[index] = 'S' if classes[i] else 'P'
    return joint('', res)


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    t = int(raw_input())
    subs = []
    for i in xrange(2*t - 2):
        s = raw_input()
        subs.append([s, i])
    print solve(subs)
