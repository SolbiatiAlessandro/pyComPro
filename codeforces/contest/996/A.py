n,res = int(input()), 0
for i in [100,20,10,5,1]:
	res+=n//i
	n = n%i
print(res)
	
