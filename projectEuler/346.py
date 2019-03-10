def main():
    N = pow(10, 12)
    b = 2
    tot = 0
    ans = set([1])
    while 1 + b + b**2 < N:
        k = 2
        num = 1 + b + b**2
        while num < N:
            ans.add(num)
            k += 1
            num += b ** k
        b += 1
    return sum(ans)
print(main())




