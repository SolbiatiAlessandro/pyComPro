n, h, a, b, k = map(int, raw_input().split())
for _ in xrange(k):
	st,sf,et,ef = map(int, raw_input().split())
        if ( sf <= a and a <= ef ) or ( sf <= b and b <= ef ):
            result = abs( st - et ) + abs( sf - ef )
        elif(sf <= a and ef <= a):
            result = abs( st - et ) + ( a - sf ) + ( a - ef )
        elif(sf >= b and ef >= b):
            result = abs(st - et) + (sf - b) + (ef - b)
        print result 
