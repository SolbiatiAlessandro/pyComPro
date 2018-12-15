from collections import defaultdict
t = int(raw_input())
def solve():
    n, m = map(int, raw_input().split())
    if m == 0: return pow(3, n) % 998244353  
    children = defaultdict(list)
    colors = {}
    for _ in xrange(m):
        a, b = map(int, raw_input().split())
        children[a-1].append(b-1)
        children[b-1].append(a-1)
    counts = [0, 0]
    visited = set()
    for x in xrange(n):
        if x not in visited:
            colors[x] = False
            counts[0] += 1
            queue = [x]
            visited.add(x)
            #import pdb;pdb.set_trace() 
            while queue:
                node = queue.pop()
                color = colors[node]
                for child in children[node]:
                    if colors.get(child) is None:
                        visited.add(child)
                        colors[child] = not color
                        counts[not color] += 1
                        queue.insert(0, child)
                    else:
                        if colors[child] == color:
                            return 0
    a = pow(2, counts[0])  
    b = pow(2, counts[1])
    return (a + b) % 998244353 
for _ in xrange(t):
    print solve()

