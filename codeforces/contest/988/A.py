n, k = map(int, input().split())
s, v = set(), []
for i, ai in enumerate(map(int, input().split())):
    if ai not in s:
        s.add(ai)
        v += [str(i+1)]
print('YES\n'+' '.join(v[:k]) if len(v) >= k else 'NO')
