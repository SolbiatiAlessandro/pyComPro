n = int( raw_input() )
a = map(int, raw_input().split())
res = [] 
for i in xrange( n ):
        #import pdb; pdb.set_trace()
        mask = [ 0 ] * (n)
        curr = i
        while mask[ curr ] == 0:
            mask[ curr ]= 1
            curr = a[ curr ] - 1
        res.append( curr+1 )
s = ""
for e in res:
    s+=str(e)+" "
print s

