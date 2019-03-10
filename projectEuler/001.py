from __future__ import division
def sum_to_n(n): return n*(n+1)/2

assert sum_to_n(3) == 6
assert 3*sum_to_n(3) == 3*6

x=1000
s3 = sum_to_n(int((x - 1)/3)) * 3
s5 = sum_to_n(int((x - 1)/5)) * 5
s15 = sum_to_n(int((x - 1)/15)) * 15
print int(s3 + s5 - s15)
