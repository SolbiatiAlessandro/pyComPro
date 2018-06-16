n, k = map(int, input().split())
power, coins, kings, res = list(map(int, input().split())), list(map(int,input().split())), [], []
for i in range(n):
    kings += [(power[i], coins[i])]
s = sorted(kings, key=lambda x: x[1], reverse=1)
for king in kings:
    cnt, base = 0, 0
    cum = 0
    while cnt < k and base < len(s):
        if s[base][0] < king[0]:
            cum += s[base][1]
            cnt += 1
        base += 1
    res += [cum+king[1]]
print(*res)

