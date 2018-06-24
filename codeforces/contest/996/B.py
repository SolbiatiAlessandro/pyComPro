import math
R = lambda : list(map(int, input().split()))
n, a, m, res = int(input()), R(), 10e9,-1
k = ((i,math.ceil((ai-i)/n)) for i,ai in enumerate(a))
for _ in range(n):
	t = next(k)
	if(t[1]<m):
		m=t[1]
		res = t[0]
print(res+1)
	
