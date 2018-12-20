for _ in xrange(int(raw_input())):
    n, k = map(int, raw_input().split()) 
    print ''.join([chr(ord('a') + i%k) for i in xrange(n)])
