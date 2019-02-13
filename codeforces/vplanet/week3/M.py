"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(start_values, neighbs):
    answers = ['*' for _ in start_values]
    def answer(node, parent):
        #print node, parent
        local_neighbs = neighbs[node]
        if not local_neighbs or (len(local_neighbs) == 1 and local_neighbs[0][0] == parent):
            answers[node] = start_values[node]
            res = start_values[node]
            return res
        else:
            biggest = 0
            big1, big2 = 0, 0
            for neigh, dist in local_neighbs:
                if neigh != parent:
                    if answers[neigh] == '*':
                        biggest = max(biggest, answer(neigh, node))
                    curr = answers[neigh] - dist
                    if curr > big1:
                        big2 = big1
                        big1 = curr
                    elif curr > big2:
                        big2 = curr

            res = start_values[node] + max(0, big1) + max(0, big2)
            biggest = max(res, biggest)
            
            answers[node] = start_values[node] + max(0, big1)
            return biggest
    res = answer(0, -1)
    return res
            

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    raw_input()
    start_values = stdin()
    from collections import defaultdict
    neighbs = defaultdict(list)
    for _ in xrange(len(start_values) - 1):
        u, v, c = stdin()
        neighbs[u-1].append((v-1, c))
        neighbs[v-1].append((u-1, c))
    print solve(start_values, neighbs)
