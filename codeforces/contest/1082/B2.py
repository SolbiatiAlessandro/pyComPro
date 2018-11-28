def solve():
    _ = int(raw_input())
    string = raw_input()
    formatted = ""
    count, tot_count = 0, 0
    for i, char in enumerate(string):
        if char == "G": count += 1
        if i == len(string) - 1 and count != 0:
            formatted += str(count)
            tot_count += count
        elif char == "S":
            if count != 0:
                formatted += str(count)+"S"
                tot_count += count
                count = 0
            else:
                formatted += "S"
    print formatted

    res = 0
    answers = [0 for x in xrange(len(formatted))]
    for i, char in enumerate(formatted):
        flip = 0
        if i - 1 >= 0 and formatted[i - 1] != "S":
            flip += int(formatted[i - 1])
        if i + 1 < len(formatted) and formatted[i + 1] != "S":
            flip += int(formatted[i + 1])
        flip += int(flip < tot_count)
        if formatted[i] != "S": flip = max(flip, int(formatted[i]))
        answers[i] = flip
        res = max(res, flip)
    print answers
    return res


print solve()
