def solve(string):
    formatted = []
    i, count = 0, 0
    while i < len(string):
        if string[i] == "G":
            count += 1
            if i + 1 == len(string): 
                formatted.append(count)
            elif string[i + 1] == "S":
                formatted.append(count)
                count = 0
        if string[i] == "S": formatted.append(0)
        i += 1
    res, tot_count = 0, sum(formatted)
    for i in xrange(len(formatted)):
        _res = formatted[i]
        if i > 0: _res += formatted[i - 1]
        if i + 1 < len(formatted): _res += formatted[i + 1]
        #answers.append(_res)
        res = max(res, _res)
    #print answers
    return res + int(res < tot_count)

if __name__ == "__main__":
    _ = int(raw_input())
    string = raw_input()
    print solve(string)
