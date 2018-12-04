n = int(raw_input())
a = map(int, raw_input().split())
def solve(n, a):
    prime = n
    added = 0
    answer = []
    print n + 1
    for i, num in enumerate(a[::-1]):
        index = len(a) - 1 - i
        target = prime - 1 - i
        add = target - ((num + added) % prime)
        if add < 0: add += prime
        answer.insert(0, (num + added + add) % prime)
        added += add
        print "1 {} {}".format(index + 1, add)
    print "2 {} {}".format(len(a), prime)
    return answer
solve(n, a)
