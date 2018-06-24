R = lambda : list(map(int, input().split()))
n,a,s = R(),R(),0
for x in a:
	s+=x
if s:
	print("YES\n1\n1 "+str(len(a)))
else:
	p,f=0,0
	for i in range(len(a)):
		p+=a[i]
		if(p!=0 and not f):
			print("YES\n2\n1 %d\n%d %d" % (i+1, i+2, len(a)))
			f=1
	if not f:
		print("NO")  
			

