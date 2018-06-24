import math
n, a, m, res = int(input()), [*(map(int,input().split()))], 10e9,-1
k = [ math.ceil((ai-i)/n) for i,ai in enumerate(a) ]
print(k.index(min(k))+1)
	
