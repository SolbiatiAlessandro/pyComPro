f=open("Dl.in","w")
f.write("1000 1000 9\n")
f.write("1 4 2 6 32 1 5 2 3\n")
for i in xrange(1, 10):
    f.write(str(i)+'.'*999+'\n')

for i in range(1000 - 9):
    f.write('.'*1000+"\n")
f.close()
