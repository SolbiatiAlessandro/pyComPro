n = int(input())
a = []
for i in range(n):
    a += [input()]


def solve(a, n):
    for i in range(n):
        for j in range(n-1):
            if a[j+1] in a[j]:
                a[j+1], a[j] = a[j], a[j+1]
            elif len(a[j+1]) < len(a[j]):
                return print("NO")
    print("YES")
    for aa in a:
        print(aa)


solve(a, n)

