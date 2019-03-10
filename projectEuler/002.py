res = 0
f, p = 1, 1
while f <= 4*int(pow(10, 6)):
    t = f
    f = p + f
    p = t
    if f % 2 == 0: res += f
    if f < 100: print f
print res
