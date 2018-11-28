def solve():
    _ = int(raw_input())
    string = raw_input()
    d = {}
    count = 0
    res = 0
    prev = None
    for i, char in enumerate(string):
        if char == 'G': count += 1
        if char == 'S':
            if prev is not None:
                d[prev][1] = count
                prev = None
            if i + 1 < len(string) and string[i + 1] == 'G' and count != 0:
                d[i] = [count, None]
                prev = i
            res = max(res, count)
            count = 0
        if i == len(string) - 1 and char == "G":
            if prev is not None:
                d[prev][1] = count
            res = max(res, count)
    print d
    if len(d) == 0: return res
    if len(d) == 1: return d.values()[0][0] + d.values()[0][1] 
    for [left, right] in d.values():
        res = max(res, left + right + 1)
    return res


print solve()
