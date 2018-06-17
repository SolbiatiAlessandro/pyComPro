R = lambda: (int, input().split())
n, a, b = R(), R(), R()
print(' '.join(map(str, (x for x in a if x in b))))


