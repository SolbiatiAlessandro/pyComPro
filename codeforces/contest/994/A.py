n, m = map(int, input().split())
a, b, res = map(int, input().split()), set(map(int, input().split())), []
for x in a:
    if x in b:
        res += [x]
print(*res)

