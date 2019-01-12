r = lambda : map(int, raw_input().split())
A, B, C = r(),r(),r()
dist = lambda A, B:  abs(A[0]-B[0]) + abs(A[1]-B[1]) + 1
AB = [dist(A,B), (A,B)]
AC = [dist(A,C), (A,C)]
CB = [dist(C,B), (C,B)]
order = sorted([AB,AC,CB])
#print order
#print order[0][0]+order[1][0]
points = [A,B,C]
def path(A,B):
    

