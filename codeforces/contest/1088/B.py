n, k  = map(int, raw_input().split())
a = map(int, raw_input().split())
a.sort()
prev = a[0]
count = 1
print prev
for i in xrange(1, n):
    if a[i] != prev and count + 1 <= k:
        print a[i] - prev
        prev = a[i]
        count += 1
for _ in xrange(k - count): print "0"

