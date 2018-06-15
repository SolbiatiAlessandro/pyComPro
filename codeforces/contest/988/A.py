from sys import stdin, stdout


def main():
    n, k = [int(x) for x in stdin.readline().split()]
    a = [int(x) for x in stdin.readline().split()]

    res = []
    support = []

    for i in range(len(a)):
        x = a[i]
        new = 1
        for y in support:
            if x == y:
                new = 0
        if new:
            support.append(x)
            res.append(i)

    if len(res) < k:
        stdout.write("NO")
    else:
        stdout.write("YES\n")
        for i in range(0, k):
            stdout.write(str(res[i]+1)+" ")


if __name__ == "__main__":
    main()
